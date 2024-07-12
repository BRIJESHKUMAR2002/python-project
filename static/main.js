function trainingFileUploaderUpdateLabel() {
  // Get the input element
  var input = document.getElementById('trainingFileUploader');
  // Get the label element
  var label = document.getElementById('trainingFileUploaderLabel');
    // Check if a file is selected
  if (input.files.length > 0) {
    // Get the selected file name
    var fileName = input.files[0].name;

    // Truncate the file name if it exceeds 25 characters
    if (fileName.length > 50) {
      fileName = fileName.substring(0, 25) + '...';
    }

    // Set the label text to the truncated file name
    label.textContent = fileName;
  } else {
    // If no file is selected, reset the label text
    label.textContent = '';
  }
}


function evaluateFileUploaderUpdateLabel() {
  // Get the input element
  var input = document.getElementById('evaluateFileUploader');
  // Get the label element
  var label = document.getElementById('evaluateFileUploaderLabel');
    // Check if a file is selected
  if (input.files.length > 0) {
    // Get the selected file name
    var fileName = input.files[0].name;

    // Truncate the file name if it exceeds 25 characters
    if (fileName.length > 50) {
      fileName = fileName.substring(0, 25) + '...';
    }

    // Set the label text to the truncated file name
    label.textContent = fileName;
  } else {
    // If no file is selected, reset the label text
    label.textContent = '';
  }
}
