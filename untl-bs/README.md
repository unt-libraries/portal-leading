Assessing the Composition of a Locally-Developed Controlled Vocabulary:
University of North Texas Libraries Browse Subjects

This study sought to assess what areas of the UNTL-BS schema (as it stood in 2022) would benefit most from having additional terms added to them, and what new terms might benefit the schema the most. All files related to this project may be found in the "untl-bs" folder of the UNTL GitHub repository. The data was generated and exported using Solr queries of the index to the Portal to Texas History, and further manipulated in Excel.

The "untl-bs" folder is composed of three main parts: "code," "data," and "visualizations."

"Code" contains the various Python scripts used to generate the datasets found in "data."

"Data" is by far the largest folder, and contains multiple sub-folders corresponding to the various stages of the study.

1. Preliminary Examinations - this folder contains some of Hannah J.'s first examinations of the UNTL-BS data.
 - "BranchPercentages" displays the total usage of the UNTL-BS schema on the Portal as a pie chart, divided into the schema's 14 main branches.
 - The two "OccurrenceRates" documents as well as the "FrequencyOfOccurrenceCounts" document compare the occurrence rates of the UNTL-BS terms against those in the custom keyword field.
 - The "collocations" folder contains data related to the Collocation Rates analysis, which captures the strength of associations between UNTL-BS terms and other subject terms on the Portal's records.

2. Outlier Analysis - this folder contains two documents, both related to identifying terms that have occurrence counts on the Portal that can be deemed statistical outliers. This was the first step in constructing the project's terms of interest list.

3. Spread Vs. Usage - this analysis formed the core of the terms of interest list. By comparing each browse subject's number of narrower terms with its occurrence count on the Portal, the analysis seeks to identify terms that may merit expansion. The first two attempts at the analysis (from September 9 and 15) were incomplete, but they illustrate the process used to identify imbalanced terms. The final version of the analysis dates from October 24, and is accompanied by a revised set of notes explaining what terms were added to the list as a result of the analysis.

4. Keyword Ratios - this analysis was the final step in constructing the project's terms of interest list. Calculating the average number of subject terms to appear alongside each browse subject throughout the Portal's records, the analysis identifies terms that are most likely to be accompanied by additional terms, with the presumption that these terms may have nuances or facets that are not yet expressed in the browse schema.

5. Redundancy - the files in this folder constitute the first of three tests conducted to identify any terms that were erroneously added to the terms of interest list. This analysis seeks to identify any browse terms that duplicate information from either of two other metadata fields (PlaceName and ResourceType).

6. Parent/Child Collocations - this second test seeks to determine whether any terms from the terms of interest list have high occurrence counts because they had been applied along with their own narrower terms or broader terms in the same branch of the schema.

7. Metadata Variability - this last test examines the diversity of values found in  three metadata fields from records containing each of the terms of interest. The goal of the analysis is to determine whether any of the terms have high occurrence counts because they were systematically applied to all or nearly all items in a particular collection, from a particular institution, or of a particular resource type.

8. Topic Modeling