---
layout: default
title: PADER: Paillier-based Secure Decentralized Social Recommendation
---

# PADER: Paillier-based Secure Decentralized Social Recommendation
**arXiv**：[2601.10212v1](https://arxiv.org/abs/2601.10212) · [PDF](https://arxiv.org/pdf/2601.10212.pdf)  
**作者**：Chaochao Chen, Jiaming Qian, Fei Zheng, Yachuan Liu  

**一句话要点**：提出基于Paillier的PADER系统，实现去中心化社交推荐以保护用户和商家隐私。

**关键词**：隐私保护推荐, 去中心化系统, Paillier加密, 社交正则化模型, 安全多方计算

## 3 点简述
- 核心问题：集中式推荐系统收集用户和商家数据引发隐私担忧。
- 方法要点：应用Paillier加密到SoReg模型，设计安全协议支持去中心化训练和推理。
- 实验或效果：实验显示单用户迭代约1秒，50万评分训练<3小时，证明实用性。

## 摘要（原文）

> The prevalence of recommendation systems also brings privacy concerns to both the users and the sellers, as centralized platforms collect as much data as possible from them. To keep the data private, we propose PADER: a Paillier-based secure decentralized social recommendation system. In this system, the users and the sellers are nodes in a decentralized network. The training and inference of the recommendation model are carried out securely in a decentralized manner, without the involvement of a centralized platform. To this end, we apply the Paillier cryptosystem to the SoReg (Social Regularization) model, which exploits both user's ratings and social relations. We view the SoReg model as a two-party secure polynomial evaluation problem and observe that the simple bipartite computation may result in poor efficiency. To improve efficiency, we design secure addition and multiplication protocols to support secure computation on any arithmetic circuit, along with an optimal data packing scheme that is suitable for the polynomial computations of real values. Experiment results show that our method only takes about one second to iterate through one user with hundreds of ratings, and training with ~500K ratings for one epoch only takes <3 hours, which shows that the method is practical in real applications. The code is available at https://github.com/GarminQ/PADER.

