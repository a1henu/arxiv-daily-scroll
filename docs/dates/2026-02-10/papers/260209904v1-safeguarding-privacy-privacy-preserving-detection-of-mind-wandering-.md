---
layout: default
title: Safeguarding Privacy: Privacy-Preserving Detection of Mind Wandering and Disengagement Using Federated Learning in Online Education
---

# Safeguarding Privacy: Privacy-Preserving Detection of Mind Wandering and Disengagement Using Federated Learning in Online Education
**arXiv**：[2602.09904v1](https://arxiv.org/abs/2602.09904) · [PDF](https://arxiv.org/pdf/2602.09904.pdf)  
**作者**：Anna Bodonhelyi, Mengdi Wang, Efe Bozkir, Babette Bühler, Enkelejda Kasneci  

**一句话要点**：提出基于联邦学习的隐私保护框架，用于在线教育中通过视频检测走神与脱离行为。

**关键词**：联邦学习, 隐私保护, 在线教育, 走神检测, 视频分析, 注视特征

## 3 点简述
- 核心问题：在线教育中学习者走神与脱离行为影响学习效果，但传统机器学习方法需共享敏感数据，引发隐私担忧。
- 方法要点：采用跨设备联邦学习，利用面部表情和注视特征训练模型，避免数据集中，并处理眼镜干扰以提升性能。
- 实验或效果：在五个数据集上验证，比较多种联邦学习算法，结果显示该方法在隐私保护下有效促进学习者参与。

## 摘要（原文）

> Since the COVID-19 pandemic, online courses have expanded access to education, yet the absence of direct instructor support challenges learners' ability to self-regulate attention and engagement. Mind wandering and disengagement can be detrimental to learning outcomes, making their automated detection via video-based indicators a promising approach for real-time learner support. However, machine learning-based approaches often require sharing sensitive data, raising privacy concerns. Federated learning offers a privacy-preserving alternative by enabling decentralized model training while also distributing computational load. We propose a framework exploiting cross-device federated learning to address different manifestations of behavioral and cognitive disengagement during remote learning, specifically behavioral disengagement, mind wandering, and boredom. We fit video-based cognitive disengagement detection models using facial expressions and gaze features. By adopting federated learning, we safeguard users' data privacy through privacy-by-design and introduce a novel solution with the potential for real-time learner support. We further address challenges posed by eyeglasses by incorporating related features, enhancing overall model performance. To validate the performance of our approach, we conduct extensive experiments on five datasets and benchmark multiple federated learning algorithms. Our results show great promise for privacy-preserving educational technologies promoting learner engagement.

