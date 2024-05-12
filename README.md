**Music Recommendation Web Based With Respect To Sonic Characterstics Using- Scann Near Neighbor Algorithm:**


This repository presents a web application and a music recommendation system which leverages a dataset of 2261 audio files after taking sample from 105 GB dataset by first classifying and then stratifying it to mirror dataset while addressing key challenges in scalability, memory efficiency, and recommendation quality. By having a combination of feature extraction techniques, efficient nearest neighbor search with tree-based SCANN algorithm, Grid Search as hyperparameter tuning, and silhouette as evaluation metrics, our approach offers a comprehensive framework for music recommendation system. This is a part of a project for the Fundamental of Big Data Analytics (DS2004) course.



**Dependencies:**


•	Librosa

•	NumPy

•	Pandas

•	Scikit-learn

•	TensorFlow

•	SCANN

•	Mongodb

•	Flask



**Introduction:**


In the realm of music recommendation systems, our solution stands out by leveraging Librosa for audio feature extraction, capturing vital characteristics like MFCC, Mel spectrograms, and Tempograms to understand musical nuances. Central to our system is the SCANN (Scalable Nearest Neighbors) algorithm, enabling efficient nearest neighbor search to identify tracks with similar rhythmic patterns and sonic characteristics, ensuring fast and accurate recommendations. With a focus on delivering personalized musical experiences, our approach prioritizes efficiency and accuracy, aiming to provide users with a seamless and delightful music discovery journey.



**Features:**

•	**Audio Feature Extraction:** Utilizes Librosa to extract MFCC, Mel spectrogram, and Tempogram features from audio files, capturing essential audio characteristics for recommendation.

•	**Recommendation System:** Implements SCANN (Scalable Nearest Neighbors) algorithm for efficient nearest neighbor search, enabling fast and accurate recommendation based on rhythmic similarity.

•	**Hyperparameter Tuning:** Utilizes grid search to optimize hyperparameters for SCANN, ensuring optimal performance in recommendation tasks.

•	**Evaluation:** Evaluates the recommendation system using the Silhouette score, providing insights into clustering quality and recommendation effectiveness.



**Limitations of Nearest Neighbor Model and SCANN through Locality Sensitive Hashing :**

•	**Scalability:**
Traditional nearest neighbor models, especially when implemented without efficient indexing structures, can struggle to scale efficiently to large datasets. As the number of items or users grows, the computational cost of calculating similarities between all pairs increases significantly, leading to performance degradation.

•	**Memory Consumption:** 
Storing the entire dataset in memory for exact nearest neighbor search can become impractical for large-scale recommendation systems. This limitation restricts the model's ability to handle massive datasets without compromising on memory usage or query speed.

•	**Curse of Dimensionality:**
In high-dimensional feature spaces, traditional nearest neighbor models may suffer from the curse of dimensionality, where the density of data points becomes sparse, making distance-based similarity measures less reliable. This phenomenon can degrade recommendation quality, especially for sparse or noisy data.



**Locality Sensitive Hashing (LSH) based SCANN:**

•	**Approximation Errors:** 
LSH-based SCANN methods trade accuracy for efficiency by approximating nearest neighbors using hash functions. While they can offer fast query processing times, especially in high-dimensional spaces, they may introduce approximation errors that degrade recommendation quality, particularly for datasets with complex structures or subtle similarities.

•	**Parameter Sensitivity:**
LSH-based SCANN methods often require careful tuning of hashing parameters to balance accuracy and efficiency. Selecting appropriate hash functions and hash table sizes can be non-trivial and may require domain expertise or extensive experimentation, making them less accessible for practitioners without specialized knowledge.

•	**Difficulty in Handling High-Dimensional Data:** LSH-based SCANN methods may struggle to handle high-dimensional data efficiently due to the curse of dimensionality. As the number of dimensions increases, the effectiveness of hash functions in preserving local similarities diminishes, leading to decreased recall and increased false positive rates in approximate nearest neighbor search.



**Overcoming these limitations through Tree-Based indexing SCANN:**

•	**Hierarchical Structure:**
Our solution incorporates tree-based indexing SCANN algorithm which organize the dataset into a hierarchical structure. This organization facilitates efficient search operations by recursively partitioning the data into smaller subsets, reducing the search space and improving query processing speed.

•	**Balanced Partitioning:** 
Tree-based SCANN algorithms strive to achieve balanced partitioning of the dataset, ensuring that each node in the tree contains a roughly equal number of data points. This balance helps maintain efficient query performance by avoiding skewed distributions that could degrade search efficiency.

•	**Dimensionality Reduction:**
Tree-based SCANN algorithms often incorporate dimensionality reduction techniques within each tree node, such as splitting the data along dimensions with high variance. This dimensionality reduction enhances search efficiency, especially in high-dimensional datasets, by effectively reducing the effective dimensionality of the search space.

•	**Adaptive Splitting Strategies:** 
Our solution utilizes adaptive splitting strategies in tree-based SCANN algorithms to optimize the tree structure based on the characteristics of the dataset. These strategies dynamically select split dimensions at each node, leading to more effective partitioning and improved search performance.



**Usage:**

•	**Data Preprocessing:**
Execute preprocessing.ipynb to preprocess audio files and extract features. This notebook will preprocess the audio files, extract features, and save them to a CSV file named **preprocessed_audios.csv.**

•	**Recommendation Model Training:**
Run recommendation_model.ipynb to train the recommendation model using the preprocessed features from **preprocessed_audios.csv**. This notebook will implement the recommendation algorithm, utilizing techniques such as SCANN for efficient nearest neighbor search.

•	**MongoDB Script Execution:**
Utilize **mongodbscript.ipynb** to interact with MongoDB and store/retrieve data as necessary. This notebook provides functionalities to store preprocessed audio features in MongoDB for efficient data management and retrieval.



**Why Our Approach is Better?**

•	**Efficiency and Accuracy:**
Our approach combines the simplicity and interpretability of nearest neighbor models with the efficiency and accuracy of tree-based SCANN algorithms, achieving a balance between recommendation quality and computational performance.

•	**Scalability and Memory Efficiency:**
Tree-based SCANN algorithms enable efficient handling of large datasets by leveraging hierarchical structures and balanced partitioning, making them suitable for recommendation systems operating on massive datasets with limited memory resources.

•	**Robustness and Flexibility:** 
Adaptive splitting strategies and parameter tuning techniques enhance robustness and flexibility, allowing practitioners to optimize performance for specific datasets and query requirements. This mitigates the limitations of traditional nearest neighbor models and LSH-based SCANN methods while offering improved scalability, accuracy, and efficiency in recommendation systems.



**Result of Recommendation System:**

Calculating silhouette score based on clustering...

Silhouette Score: 0.2252306704302388

 
path_to_your_audio_file.mp3 /home/mutayyab/Documents/dataset/091/091125.mp3

 
Top 10 Recommendations Based on Rhythmic Similarity:

 
Recommended Track: 091643.mp3 - Similarity Score: 0.369567334651947

Recommended Track: 091992.mp3 - Similarity Score: 0.3840720057487488

Recommended Track: 090003.mp3 - Similarity Score: 0.44844454526901245

Recommended Track: 093442.mp3 - Similarity Score: 0.4810391068458557

Recommended Track: 091635.mp3 - Similarity Score: 0.4901089072227478

Recommended Track: 091773.mp3 - Similarity Score: 0.5003558993339539

Recommended Track: 092273.mp3 - Similarity Score: 0.5029585659503937

Recommended Track: 091828.mp3 - Similarity Score: 0.5037169456481934

Recommended Track: 091268.mp3 - Similarity Score: 0.5423231720924377

Recommended Track: 092201.mp3 - Similarity Score: 0.5428546667098999



**Contributors:**

•	**M.Muttayab** (22i-1949)

•	**M.Abubakar** (22i-2003)
