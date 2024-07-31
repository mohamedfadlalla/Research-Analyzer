from langchain.prompts import PromptTemplate
import util
import pandas as pd

get_clarity = PromptTemplate.from_template("""
###instructions###
You will be provided with the method section and the abstract of my study you job is to critzie for Clarity and Reproducibility it as follows: 

**What to Look For:**
- Detailed descriptions of procedures
- Specifics about materials and equipment
- Step-by-step protocols
- Clear instructions on how to perform experiments or analyses

**Step-by-Step Critique Process:**
1. **Read Through the Method Section**: Read the entire method section to get a general understanding of the procedures.
2. **Identify Key Procedures**: Note down the main steps or stages of the methodology.
3. **Check for Detail**: Ensure each procedure is described in enough detail. Ask if you could replicate the experiment exactly as described.
4. **List Materials and Equipment**: Confirm that all necessary materials and equipment are listed, including specific brands or models if relevant.
5. **Evaluate the Order and Logic**: Ensure the steps are presented in a logical order that follows the experimental timeline.
6. **Look for Ambiguities**: Identify any ambiguous terms or vague descriptions that could lead to confusion or variability in replication.
7. **Compare with Standards**: Compare the descriptions with standard practices or protocols in the field to see if they meet expected norms.

###abstract###
{abstract}

###method section###
{method}

###Critique###

""")



















"""
### 2. Appropriateness and Justification
**What to Look For:**
- Relevance of methods to research questions or hypotheses
- Justifications for the choice of methods
- References to established protocols or previous studies
- Suitability of the methods for the type of data collected

**Step-by-Step Critique Process:**
1. **Identify Research Questions**: Clearly identify the research questions or hypotheses stated in the paper.
2. **Match Methods to Questions**: Determine if the methods used are appropriate for answering these questions or testing these hypotheses.
3. **Review Justifications**: Look for explanations as to why these particular methods were chosen. Check if the authors have referenced other studies or standard protocols.
4. **Assess Method Suitability**: Evaluate if the methods are suitable for the type of data being collected (e.g., qualitative vs. quantitative).
5. **Compare Alternatives**: Consider if there are alternative methods that might be more appropriate or if the chosen methods have known limitations.
6. **Check References**: Verify that the cited references for the methods are appropriate and relevant to the current study.
7. **Evaluate Novel Methods**: If novel methods are used, assess whether they are adequately validated and justified.

### 3. Bias and Limitations
**What to Look For:**
- Potential sources of bias
- Handling of control groups and variables
- Confounding factors and how they are addressed
- Acknowledgment of methodological limitations

**Step-by-Step Critique Process:**
1. **Identify Control Groups**: Determine if appropriate control groups are included and described.
2. **Evaluate Variable Handling**: Check how variables are defined, measured, and controlled. Ensure key variables are accounted for and properly managed.
3. **Spot Potential Biases**: Look for any sources of bias, such as selection bias, measurement bias, or procedural bias.
4. **Identify Confounding Factors**: Determine if there are any potential confounding factors that could impact the results and check how they are addressed.
5. **Review Limitations Acknowledged**: See if the authors have acknowledged any limitations of their methodology.
6. **Check for Mitigation Strategies**: Assess if the authors have implemented strategies to mitigate biases and limitations.
7. **Consider Impact on Results**: Think about how the identified biases and limitations might affect the study’s conclusions or reliability.

By following these step-by-step processes, you can provide a thorough and structured critique of the method section in a research paper."""