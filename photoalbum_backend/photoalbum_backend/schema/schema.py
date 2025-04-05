# photoalbum_backend/schema/schema.py
import graphene
from graphene_django import DjangoObjectType
from photos.models import Photo
from graphql_jwt.decorators import login_required

class PhotoType(DjangoObjectType):
    class Meta:
        model = Photo
        fields = ("id", "title", "image", "description", "upload_date", "created_at", "updated_at")

class Query(graphene.ObjectType):
    all_photos = graphene.List(PhotoType)
    photo = graphene.Field(PhotoType, id=graphene.Int())

    def resolve_all_photos(root, info, **kwargs):
        return Photo.objects.all().order_by('-upload_date')

    def resolve_photo(root, info, id):
        return Photo.objects.get(pk=id)

class CreatePhoto(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        image = graphene.String(required=True)  # Base64 encoded image
        description = graphene.String()

    photo = graphene.Field(PhotoType)

    @classmethod
    @login_required
    def mutate(cls, root, info, title, image, description=None):
        import base64
        from django.core.files.base import ContentFile
        
        format, imgstr = image.split(';base64,') 
        ext = format.split('/')[-1] 
        data = ContentFile(base64.b64decode(imgstr), name=f'photo.{ext}')
        
        photo = Photo(
            title=title,
            image=data,
            description=description
        )
        photo.save()
        return CreatePhoto(photo=photo)

class Mutation(graphene.ObjectType):
    create_photo = CreatePhoto.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)