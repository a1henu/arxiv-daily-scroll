---
layout: default
title: TALON: Test-time Adaptive Learning for On-the-Fly Category Discovery
---

# TALON: Test-time Adaptive Learning for On-the-Fly Category Discovery
**arXiv**：[2603.08075v1](https://arxiv.org/abs/2603.08075) · [PDF](https://arxiv.org/pdf/2603.08075.pdf)  
**作者**：Yanan Wu, Yuhan Yan, Tailai Chen, Zhixiang Chi, ZiZhang Wu, Yi Jin, Yang Wang, Zhenbo Li  

**一句话要点**：提出TALON测试时自适应学习框架，以解决在线类别发现中固定知识库和特征量化的问题。

**关键词**：在线类别发现, 测试时自适应学习, 原型更新, 编码器更新, 类别爆炸缓解

## 3 点简述
- 核心问题：现有方法冻结特征提取器并量化特征，导致信息损失和类别爆炸，忽视新数据学习潜力。
- 方法要点：结合语义感知原型更新和稳定测试时编码器更新，动态扩展知识库，并离线阶段引入边距感知逻辑校准。
- 实验或效果：在标准基准上显著超越现有哈希方法，提高新类别准确率并有效缓解类别爆炸。

## 摘要（原文）

> On-the-fly category discovery (OCD) aims to recognize known categories while simultaneously discovering novel ones from an unlabeled online stream, using a model trained only on labeled data. Existing approaches freeze the feature extractor trained offline and employ a hash-based framework that quantizes features into binary codes as class prototypes. However, discovering novel categories with a fixed knowledge base is counterintuitive, as the learning potential of incoming data is entirely neglected. In addition, feature quantization introduces information loss, diminishes representational expressiveness, and amplifies intra-class variance. It often results in category explosion, where a single class is fragmented into multiple pseudo-classes. To overcome these limitations, we propose a test-time adaptation framework that enables learning through discovery. It incorporates two complementary strategies: a semantic-aware prototype update and a stable test-time encoder update. The former dynamically refines class prototypes to enhance classification, whereas the latter integrates new information directly into the parameter space. Together, these components allow the model to continuously expand its knowledge base with newly encountered samples. Furthermore, we introduce a margin-aware logit calibration in the offline stage to enlarge inter-class margins and improve intra-class compactness, thereby reserving embedding space for future class discovery. Experiments on standard OCD benchmarks demonstrate that our method substantially outperforms existing hash-based state-of-the-art approaches, yielding notable improvements in novel-class accuracy and effectively mitigating category explosion. The code is publicly available at \textcolor{blue}{https://github.com/ynanwu/TALON}.

