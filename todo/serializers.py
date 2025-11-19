

from rest_framework import serializers, validators

from todo.models import Task


class TaskSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=255, validators=[
        validators.UniqueValidator(Task.objects.all())
    ])
    description = serializers.CharField(max_length=255)




    def create(self, validated_data):
        task = Task.objects.create(
            title=validated_data["title"],
            description = validated_data["description"],


        )

        return task

    def update(self, instance, validated_data):
        # Обновляем поля экземпляра
        instance.title = validated_data.get('title', instance.title)
        # Проверяем наличие description
        if 'description' in validated_data:
            instance.description = validated_data['description']
        # Сохраняем изменения
        instance.save()
        return instance

