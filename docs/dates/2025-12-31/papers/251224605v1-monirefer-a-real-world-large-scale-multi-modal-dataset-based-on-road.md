---
layout: default
title: MoniRefer: A Real-world Large-scale Multi-modal Dataset based on Roadside Infrastructure for 3D Visual Grounding
---

# MoniRefer: A Real-world Large-scale Multi-modal Dataset based on Roadside Infrastructure for 3D Visual Grounding
**arXiv**：[2512.24605v1](https://arxiv.org/abs/2512.24605) · [PDF](https://arxiv.org/pdf/2512.24605.pdf)  
**作者**：Panquan Yang, Junfei Huang, Zongzhangbao Yin, Yingsong Hu, Anni Xu, Xinyi Luo, Xueqi Sun, Hai Wu, Sheng Ao, Zhaoxing Zhu, Chenglu Wen, Cheng Wang  

**一句话要点**：提出MoniRefer数据集和Moni3DVG方法，以解决路边监控场景的3D视觉定位问题。

**关键词**：3D视觉定位, 路边监控, 多模态数据集, 点云处理, 自然语言理解, 交通场景分析

## 3 点简述
- 核心问题：现有3D视觉定位数据集和方法主要关注室内和驾驶场景，缺乏基于路边基础设施的多模态数据。
- 方法要点：构建首个大规模真实世界路边监控数据集，包含点云和文本对，并提出端到端多模态特征学习方法。
- 实验或效果：在提出的基准上进行了广泛实验和消融研究，验证了方法的优越性和有效性。

## 摘要（原文）

> 3D visual grounding aims to localize the object in 3D point cloud scenes that semantically corresponds to given natural language sentences. It is very critical for roadside infrastructure system to interpret natural languages and localize relevant target objects in complex traffic environments. However, most existing datasets and approaches for 3D visual grounding focus on the indoor and outdoor driving scenes, outdoor monitoring scenarios remain unexplored due to scarcity of paired point cloud-text data captured by roadside infrastructure sensors. In this paper, we introduce a novel task of 3D Visual Grounding for Outdoor Monitoring Scenarios, which enables infrastructure-level understanding of traffic scenes beyond the ego-vehicle perspective. To support this task, we construct MoniRefer, the first real-world large-scale multi-modal dataset for roadside-level 3D visual grounding. The dataset consists of about 136,018 objects with 411,128 natural language expressions collected from multiple complex traffic intersections in the real-world environments. To ensure the quality and accuracy of the dataset, we manually verified all linguistic descriptions and 3D labels for objects. Additionally, we also propose a new end-to-end method, named Moni3DVG, which utilizes the rich appearance information provided by images and geometry and optical information from point cloud for multi-modal feature learning and 3D object localization. Extensive experiments and ablation studies on the proposed benchmarks demonstrate the superiority and effectiveness of our method. Our dataset and code will be released.

