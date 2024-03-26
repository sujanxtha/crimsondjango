from django.shortcuts import render
from .forms import UploadFileForm
from .resources import MyDataResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponseRedirect

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                # Create a resource instance for importing
                mydata_resource = MyDataResource()
                dataset = Dataset()
                
                # Open the file in text mode and load into the dataset
                with file.open('r') as f:
                    dataset.load(f.read(), format='csv')
                
                # Import the data
                result = mydata_resource.import_data(dataset, dry_run=False)
                if not result.has_errors():
                    messages.success(request, 'Data imported successfully.')
                    return HttpResponseRedirect('success/')  # Redirect to success page
                else:
                    # If there are errors during import, display them to the user
                    messages.error(request, 'There were errors importing the data.')
                    return render(request, 'upload.html', {'form': form})
            except Exception as e:
                # Handle any other exceptions
                messages.error(request, f'Error: {e}')
                return render(request, 'upload.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def success(request):
    return render(request, 'success.html')
