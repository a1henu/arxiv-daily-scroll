---
layout: default
title: Netflix Artwork Personalization via LLM Post-training
---

# Netflix Artwork Personalization via LLM Post-training
**arXiv**：[2601.02764v1](https://arxiv.org/abs/2601.02764) · [PDF](https://arxiv.org/pdf/2601.02764.pdf)  
**作者**：Hyunji Nam, Sejoon Oh, Emma Kong, Yesu Feng, Moumita Bhattacharya  

**一句话要点**：提出基于LLM后训练的个性化艺术作品推荐方法，以提升Netflix用户满意度与参与度。

**关键词**：个性化推荐, LLM后训练, 艺术作品选择, 用户偏好建模, Netflix应用

## 3 点简述
- 核心问题：针对用户偏好多样性，解决Netflix艺术作品个性化推荐问题。
- 方法要点：对预训练LLM进行后训练，根据用户偏好选择标题的最优视觉表示。
- 实验或效果：使用Llama 3.1 8B模型，在5K测试集上比Netflix生产模型提升3-5%。

## 摘要（原文）

> Large language models (LLMs) have demonstrated success in various applications of user recommendation and personalization across e-commerce and entertainment. On many entertainment platforms such as Netflix, users typically interact with a wide range of titles, each represented by an artwork. Since users have diverse preferences, an artwork that appeals to one type of user may not resonate with another with different preferences. Given this user heterogeneity, our work explores the novel problem of personalized artwork recommendations according to diverse user preferences. Similar to the multi-dimensional nature of users' tastes, titles contain different themes and tones that may appeal to different viewers. For example, the same title might feature both heartfelt family drama and intense action scenes. Users who prefer romantic content may like the artwork emphasizing emotional warmth between the characters, while those who prefer action thrillers may find high-intensity action scenes more intriguing. Rather than a one-size-fits-all approach, we conduct post-training of pre-trained LLMs to make personalized artwork recommendations, selecting the most preferred visual representation of a title for each user and thereby improving user satisfaction and engagement. Our experimental results with Llama 3.1 8B models (trained on a dataset of 110K data points and evaluated on 5K held-out user-title pairs) show that the post-trained LLMs achieve 3-5\% improvements over the Netflix production model, suggesting a promising direction for granular personalized recommendations using LLMs.

