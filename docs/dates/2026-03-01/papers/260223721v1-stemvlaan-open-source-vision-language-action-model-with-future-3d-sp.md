---
layout: default
title: StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation
---

# StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation
**arXiv**：[2602.23721v1](https://arxiv.org/abs/2602.23721) · [PDF](https://arxiv.org/pdf/2602.23721.pdf)  
**作者**：Jiasong Xiao, Yutao She, Kai Li, Yuyang Sha, Ziang Cheng, Ziang Tong  

**一句话要点**：提出StemVLA模型，通过融合未来3D空间知识与历史4D时空表示，提升机器人长时程任务性能。

**关键词**：视觉-语言-动作模型, 3D空间预测, 4D时空表示, 机器人操作, 长时程决策, 视频几何Transformer

## 3 点简述
- 现有VLA模型依赖2D视觉到动作的直接映射，缺乏对3D空间结构和时间动态的显式建模，限制空间推理和长时程决策。
- StemVLA引入预测的未来3D空间几何知识和基于视频几何Transformer提取的历史4D时空表示，增强世界理解。
- 在CALVIN ABC-D基准测试中，StemVLA显著提升长时程任务成功率，达到未知的序列长度，表现优异。

## 摘要（原文）

> Vision-language-action (VLA) models integrate visual observations and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However, most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly modeling the underlying 3D spatial structure or temporal world dynamics. Such representations may limit spatial reasoning and long-horizon decision-making in dynamic environments. To address this limitation, we propose StemVLA, a novel framework that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations into action prediction. First, instead of relying solely on observed images, StemVLA forecasts structured 3D future spatial-geometric world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations. Second, to capture temporal consistency and motion dynamics, we feed historical image frames into a pretrained video-geometry transformer backbone to extract implicit 3D world representations, and further aggregate them across time using a temporal attention module, termed VideoFormer [20], forming a unified 4D historical spatiotemporal representation. By jointly modeling 2D observations, predicted 3D future structure, and aggregated 4D temporal dynamics, StemVLA enables more comprehensive world understanding for robot manipulation. Extensive experiments in simulation demonstrate that StemVLA significantly improves long-horizon task success and achieves state-of-the-art performance on the CALVIN ABC-D benchmark [46], achieving an average sequence length of XXX.

