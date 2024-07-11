method_1 = """
## Methods Workfow Search Strategy

During the period of COVID-19, the scientifc community had published an immense number of studies about repurposing drugs for COVID-19. These studies are scattered on the internet, and no one database will be inclusive enough to all of these studies, aside from Google Scholar. All studies have been collected by the end of 2020/12/30. In order to achieve an efcient search strategy, the following combinations of keywords were applied during the research in the Google Scholar database: (COVID19 OR SARS-CoV-2) AND (Drug repurposing OR Drug repositioning OR Drug re-profling OR Drug rediscovery) AND (Docking AND Molecular dynamic).

## Data Selection And Extraction

Titles and abstracts were frst checked for eligibility using specifc inclusion and exclusion criteria (Table 1). Selected paper were then completely reviewed as a second stage, while articles that met the exclusion criteria were eliminated.

Primarily, searching revealed a total of 405 articles, after applying the above mentioned criteria above, we ended up with 92 research articles, as presented in the fow diagram 
(Fig. 1). We further classifed them according to SARSCoV-2 targets: 73 for the main protease, 11 for spike protein, and 8 for replicase complex.

## Pharmacophore Analysis

To perform the pharmacophore study, we had to ensure that all the drugs analyzed bind to the same site on the target. Thus, we classifed the drug within the same target according to the binding site. There are various approaches used in literature to defne the binding site or the docking site. Nevertheless, we obtained one binding site for each target except the main protease; it gave us two binding sites. Phase from Schrodinger suits was used to generate the pharmacophore hypothesis [11]. As the quality of the pharmacophore was our biggest concern, we used the number of features and the Hyposcore as a measure of quality. The following criteria were implemented: a maximum of 7 features, a minimum of 6 features, and minimum coverage of 50% of the compounds at the question.

## Data Description

In silico work on COVID-19, drug discovery started even before the PDB structure of SARS-CoV-2 targets was released; during that time, homology modeling was used to generate the protein structure in question. The generated targets that have been investigated are spike protein, RNA-dependent RNA polymerase (RdRp), main protease, helicase, and papain-like protease. However, from them, we reviewed only the most studied targets (main protease, spike protein, and RdRp) [1, 2].

All papers follow a similar protocol, as shown in Fig. 2a either docking alone or docking and molecular dynamics simulation.

As illustrated in Fig. 2b, the most used software for molecular docking was Autodock vina, followed by Glide and preceded by Autodock 4. The open source feature of Autodock rationalizes its greatest usage frequency. Autodock vina is the most used because it is easier to use compare to Autodock4, and it has have been implemented in many software packages like PyRx. In addition, Autodock vina is faster and more accurate depending on the system and the parameter setting [12].

While docking studies consider the flexibility of the ligand as a rigid structure, molecular dynamic (MD) simulation takes the ligand–protein complex as a dynamic module. It searches the conformational space for the most stable conformation, giving more accurate results. Moreover, due to the cost of running MD simulation, only 48 studies out of 89 confrmed docking results with MD (Fig. 2a). GROMACS 

"""

method_2 = """
## Method: Similarity Calculation:

Drug-protein complex preparation: All of the approved drugs were obtained from drugbank.ca, then the HET code of these drugs was obtained from http://ligand-expo.rcsb.org/. The list of HET codes was used to search on RCSB pdb, excluding the compound that appeared on more than 100 per structure because most of them are either small or not specific. A total of 4400 structures were retrieved from the RCSB database. After which all the pdbs were fed to a python script to clean the pdbs and leave only the drug and the chain that it binds to, the python script was designed to get all drugs even if they are in a single pdb structure and separate them in different pdbs. After which this list of pdb files was fed to Fpocket[11] to acquire the pockets of all the pdbs. Another python script which calculates pockets Center of mass. Also, the center of masses of each drug was calculated. After that, the distance between the Center of mass of the pocket and Center of mass of the drug was calculated to output a list of distances between the drug and all of the pockets of the protein.

Then the smallest distance was chosen and the pocket that corresponds to this distance was output as a pdb file, doing this to all the drugs to obtain a list of all of the pockets of the drugs.

## Covid-19 Pockets **Preparation:**

All of the pdbs of COVID-19 were retrieved from RCSB and their chains are separated into different pdbs using a python script. After that, the pdbs were feed to Fpocket. Then all of the pockets predicted by Fpocket were output into pdbs containing the aminoacid predicted by Fpocket using another python script.

## Pocket **Comparison:**

The list of the pockets of the drugs and the pockets of COVID-19 were feed to PocketMatch[12] algorithm which works by representing each Binding site by a 90 list of sorted distances capturing the shape and chemical nature of the pocket, the sorted arrays are then aligned using an incremental alignment method and score them obtain PMscore for a pair of pockets. This algorithm is fast and only takes 1/125 for a single comparison. The calculation carried on a Linux virtual machine (4GB ram and single processor 14GB disc space), and due to the limited computational power, the similarity calculation was separated into 3 batches. PocketMatch gave two similarity measures Pmin and Pmax. In this study, Pmax was used which takes the global similarity into account and it's more strict. Pmin was ignored as the PocketMatch created said: "it's too optimistic".

## Docking Calculation:

Docking of the drug with similar pockets: The drugs that their pockets scored 0.6 on Pmax were considered for docking, swissdock[13][14] was used for docking because it takes the whole protein into account which is important to test whether the drug would bind to the pocket predicted by Fpocket or not. Thus the final results use three criteria 1\ the drug has to bind to the pocket predicted by Fpocket and 2\ it has to bind with dG less than (-8.0), 3\ and the predicted pose has to be the top pose. The results were analysed using chimera 1.13.1 [15]. Steroidal pocket *analysis:* Due to the significant big number of steroidal drugs predicted to have pocket similarity with SARS CoV 2 protein, all of the steroidal pockets were aligned using the MatchMaker tool in chimera figure(5).

"""