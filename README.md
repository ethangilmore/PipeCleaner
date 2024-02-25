# Pipe Cleaner

Pipe Cleaner is an application to clean the data output from FragPipe and MSFragger. Pipe Cleaner makes it easy to filter data using peptide accuracy, protein keywords, and post translational modifications.

# Installation



# Use

## Input Files

Pipe cleaner is made to be used with multiple input files. These files are organized into "Groups" and each group can be comprised of multiple files. For example, a control group can be made up of 4 files, and an expirement group can be made up of another 4 files.

To create a group, click the "Add Group" button, and input a name for the group. If you are working with more than one group, this will add a column to the spreadsheet with the group name. You can press "Remove Group" to delete the most recently created group. Note that there cannot be two groups with the same name.

## Apply Filters

Pipe cleaner currently comes with 3 built in filters. These filters can be toggeled on and off using the checkbox in the upper left corner.

### Filter by Probability

To filter peptides by probability, first select the column containing the accuracy using the dropdown menu. Then input the desired accuracy threshold. This will discard any peptides with accuracy less than the input threshold, and keep peptides with accuracty greater than or equal to the threshold.

### Exclude Proteins

To remove peptides from possible contaminant proteins, first select the column containing protein descriptions. Then type as many keywords (case insensitive) as you'd like into the text input, separated by commas (ex. "keratin, trypsin"). Pipe Cleaner will exclude any rows that contain any of the provided keywords in the selected column.

### Filter by Modification

To only keep peptides that were assigned modifications, first select the column containing the modification information. Then select the checkboxes for the modifications you want to keep. Note you can change the regex template used for matching modifications, but the default should work for FragPipe and MSFragger outputs.

## Output Files

At the bottom of the application, you will be able to preview the resulting spreadsheet. If everything looks good, you can press the "Export" button to save the cleaned data as a .csv, .tsv, or .xlsx file for downstream analysis.
