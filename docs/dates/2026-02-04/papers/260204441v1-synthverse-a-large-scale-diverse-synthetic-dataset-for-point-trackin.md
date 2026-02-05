---
layout: default
title: SynthVerse: A Large-Scale Diverse Synthetic Dataset for Point Tracking
---

# SynthVerse: A Large-Scale Diverse Synthetic Dataset for Point Tracking
**arXiv**：[2602.04441v1](https://arxiv.org/abs/2602.04441) · [PDF](https://arxiv.org/pdf/2602.04441.pdf)  
**作者**：Weiguang Zhao, Haoran Xu, Xingyu Miao, Qin Zhao, Rui Zhang, Kaizhu Huang, Ning Gao, Peizhou Cao, Mingze Sun, Mulin Yu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang  

**一句话要点**：提出SynthVerse大规模合成数据集以解决点跟踪数据多样性不足问题

**关键词**：点跟踪, 合成数据集, 数据多样性, 泛化评估, 动态交互, 轨迹标注

## 3 点简述
- 点跟踪面临高质量数据有限，现有数据集多样性和轨迹标注不完善。
- SynthVerse引入新领域如动画风格、具身操作，扩展对象类别和动态交互。
- 实验表明训练提升泛化能力，并揭示现有跟踪器在多样设置下的局限性。

## 摘要（原文）

> Point tracking aims to follow visual points through complex motion, occlusion, and viewpoint changes, and has advanced rapidly with modern foundation models. Yet progress toward general point tracking remains constrained by limited high-quality data, as existing datasets often provide insufficient diversity and imperfect trajectory annotations. To this end, we introduce SynthVerse, a large-scale, diverse synthetic dataset specifically designed for point tracking. SynthVerse includes several new domains and object types missing from existing synthetic datasets, such as animated-film-style content, embodied manipulation, scene navigation, and articulated objects. SynthVerse substantially expands dataset diversity by covering a broader range of object categories and providing high-quality dynamic motions and interactions, enabling more robust training and evaluation for general point tracking. In addition, we establish a highly diverse point tracking benchmark to systematically evaluate state-of-the-art methods under broader domain shifts. Extensive experiments and analyses demonstrate that training with SynthVerse yields consistent improvements in generalization and reveal limitations of existing trackers under diverse settings.

