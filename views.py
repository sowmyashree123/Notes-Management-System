from django.shortcuts import render, redirect
from .models import Note
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

# ADD NOTE
def add_note(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']

        Note.objects.create(
            title=title,
            content=content
        )

        return redirect('/view-notes/')

    return render(request, 'add_note.html')


# VIEW NOTES
def view_notes(request):
    query = request.GET.get('q')

    if query:
        notes = Note.objects.filter(title__icontains=query)
    else:
        notes = Note.objects.all()

    return render(request, 'view_notes.html', {'notes': notes})


# DELETE NOTE
def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()

    return redirect('/view-notes/')

def edit_note(request, id):
    note = Note.objects.get(id=id)

    if request.method == "POST":
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()

        return redirect('/view-notes/')

    return render(request, 'edit_note.html', {'note': note})

@api_view(['GET'])
def api_get_notes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def api_add_note(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def api_delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return Response({"message": "Deleted"})
@api_view(['PUT'])
def api_update_note(request, id):
    note = Note.objects.get(id=id)
    serializer = NoteSerializer(note, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def api_search_notes(request):
    query = request.GET.get('q')

    if query:
        notes = Note.objects.filter(title__icontains=query)
    else:
        notes = Note.objects.all()

    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)