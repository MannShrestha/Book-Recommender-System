<div align="justify">
# Book-Recommender-System

## Dataset Link: 
- https://www.kaggle.com/datasets/mostafanofal/book-crossing-descriptions-from-google-api/data


## Recommender Systems Survey

```text
Recommender Systems
│
├── 1. Collaborative Filtering
│   ├── User-based CF
│   ├── Item-based CF
│   └── Matrix Factorization
│       ├── SVD
│       ├── NMF
│       └── ALS
│
├── 2. Content-Based Filtering
│
├── 3. Hybrid Recommendation
│   ├── Weighted Hybrid
│   └── Switching Hybrid
│
├── 4. Deep Learning
│   ├── NCF (Neural Collaborative Filtering)
│   ├── AutoRec
│   ├── GRU4Rec (Session-based Recommendation)
│   ├── SASRec (Self-Attention)
│   └── BERT4Rec
│
├── 5. Graph-based Recommendation
│   ├── NGCF
│   └── LightGCN
│
├── 6. Reinforcement Learning
│   └── DQN-based Recommendation
│
├── 7. Context-Aware Recommendation
│   ├── CARS
│   └── Factorization Machines
│
└── 8. Knowledge Graph Recommendation
    └── TransE-based Recommendation

```
## Journal **A Comprehensive Review of Recommender Systems: Transitioning from Theory to Practice**
- link: https://arxiv.org/pdf/2407.13699


# Problem Statement

The objective of this project is to develop a personalised book recommendation system that can recommend books to users based on patterns observed in previous user-book interactions. The dataset contains information about books, including ISBN, title, author, publication year, publisher, and cover images, together with anonymised user information and book ratings. The ratings are either explicit, ranging from 1 to 10, or implicit, represented by 0. Since users typically interact with only a small proportion of the available books, the resulting user-book interaction matrix is highly sparse. To address this problem, I propose an item-based collaborative filtering approach using the unsupervised Nearest Neighbours algorithm provided by Scikit-learn. Rather than relying on book metadata, the proposed system identifies books with similar user-rating patterns and recommends books that are closely related to those a user has previously interacted with.

# Why Item-Based Collaborative Filtering?

I selected item-based collaborative filtering because the primary objective is to identify books that are similar based on users' historical interactions. In this approach, each book is represented by the ratings or interactions it has received from users. The system then compares these interaction patterns to determine which books are most similar to one another.

For example, if many users who rated Book A highly also rated Book B highly, the system can identify these two books as similar. Consequently, when a user interacts positively with Book A, Book B can be considered a suitable recommendation.

This approach is particularly appropriate for this dataset because it allows the recommendation system to learn from collective user behaviour without requiring detailed semantic analysis of the book content. Although the dataset provides information such as author, publisher, and publication year, these attributes are not required for the proposed collaborative filtering model. Instead, the recommendation process is driven by the relationships observed within the user-book interaction data.

# Proposed Recommendation Approach

The proposed system therefore follows an item-based collaborative filtering framework using unsupervised K-Nearest Neighbours. Books are represented through their user-rating patterns, and the resulting sparse interaction matrix is stored using CSR(Compressed Sparse Row) format. NN is then applied to identify neighbouring books based on their similarity in the interaction space. The recommendations are consequently derived from collective user behaviour rather than from manually defined book characteristics.

