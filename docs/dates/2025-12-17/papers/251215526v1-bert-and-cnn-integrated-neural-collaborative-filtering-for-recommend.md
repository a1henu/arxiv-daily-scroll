---
layout: default
title: BERT and CNN integrated Neural Collaborative Filtering for Recommender Systems
---

# BERT and CNN integrated Neural Collaborative Filtering for Recommender Systems
**arXiv**：[2512.15526v1](https://arxiv.org/abs/2512.15526) · [PDF](https://arxiv.org/pdf/2512.15526.pdf)  
**作者**：Abdullah Al Munem, Sumona Yeasmin, Mohammad Rezwanul Huq  

**一句话要点**：提出集成BERT与CNN的神经协同过滤模型，以提升推荐系统性能，处理多模态数据。

**关键词**：推荐系统, 神经协同过滤, 多模态数据, BERT模型, CNN模型, MovieLens数据集

## 3 点简述
- 核心问题：推荐系统需处理用户和物品的多模态数据（数值、分类、图像）以提升推荐准确性。
- 方法要点：结合BERT处理文本特征和CNN处理图像特征，构建神经协同过滤模型，提取潜在特征。
- 实验或效果：在MovieLens数据集上验证，模型在召回率和命中率上优于基线NCF和BERT-NCF模型。

## 摘要（原文）

> Every day, a significant number of users visit the internet for different needs. The owners of a website generate profits from the user interaction with the contents or items of the website. A robust recommendation system can increase user interaction with a website by recommending items according to the user's unique preferences. BERT and CNN-integrated neural collaborative filtering (NCF) have been proposed for the recommendation system in this experiment. The proposed model takes inputs from the user and item profile and finds the user's interest. This model can handle numeric, categorical, and image data to extract the latent features from the inputs. The model is trained and validated on a small sample of the MovieLens dataset for 25 epochs. The same dataset has been used to train and validate a simple NCF and a BERT-based NCF model and compared with the proposed model. The proposed model outperformed those two baseline models. The obtained result for the proposed model is 0.72 recall and 0.486 Hit Ratio @ 10 for 799 users on the MovieLens dataset. This experiment concludes that considering both categorical and image data can improve the performance of a recommendation system.

