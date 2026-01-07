---
layout: default
title: LOST-3DSG: Lightweight Open-Vocabulary 3D Scene Graphs with Semantic Tracking in Dynamic Environments
---

# LOST-3DSG: Lightweight Open-Vocabulary 3D Scene Graphs with Semantic Tracking in Dynamic Environments
**arXiv**：[2601.02905v1](https://arxiv.org/abs/2601.02905) · [PDF](https://arxiv.org/pdf/2601.02905.pdf)  
**作者**：Sara Micol Ferraina, Michele Brienza, Francesco Argenziano, Emanuele Musumeci, Vincenzo Suriani, Domenico D. Bloisi, Daniele Nardi  

**一句话要点**：提出LOST-3DSG，一种轻量级开放词汇3D场景图，用于动态环境中的语义目标跟踪。

**关键词**：3D场景图, 动态目标跟踪, 开放词汇表示, 语义嵌入, 轻量级模型, 机器人视觉

## 3 点简述
- 核心问题：动态环境中目标跟踪效率低，现有方法依赖重型基础模型。
- 方法要点：基于word2vec和句子嵌入的语义实体跟踪，避免存储密集CLIP视觉特征。
- 实验或效果：在TIAGo机器人真实3D环境中评估，展示高效动态目标跟踪性能。

## 摘要（原文）

> Tracking objects that move within dynamic environments is a core challenge in robotics. Recent research has advanced this topic significantly; however, many existing approaches remain inefficient due to their reliance on heavy foundation models. To address this limitation, we propose LOST-3DSG, a lightweight open-vocabulary 3D scene graph designed to track dynamic objects in real-world environments. Our method adopts a semantic approach to entity tracking based on word2vec and sentence embeddings, enabling an open-vocabulary representation while avoiding the necessity of storing dense CLIP visual features. As a result, LOST-3DSG achieves superior performance compared to approaches that rely on high-dimensional visual embeddings. We evaluate our method through qualitative and quantitative experiments conducted in a real 3D environment using a TIAGo robot. The results demonstrate the effectiveness and efficiency of LOST-3DSG in dynamic object tracking. Code and supplementary material are publicly available on the project website at https://lab-rococo-sapienza.github.io/lost-3dsg/.

