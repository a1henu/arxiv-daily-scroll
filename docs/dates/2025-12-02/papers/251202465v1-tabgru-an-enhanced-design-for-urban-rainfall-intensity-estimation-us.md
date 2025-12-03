---
layout: default
title: TabGRU: An Enhanced Design for Urban Rainfall Intensity Estimation Using Commercial Microwave Links
---

# TabGRU: An Enhanced Design for Urban Rainfall Intensity Estimation Using Commercial Microwave Links
**arXiv**：[2512.02465v1](https://arxiv.org/abs/2512.02465) · [PDF](https://arxiv.org/pdf/2512.02465.pdf)  
**作者**：Xingwang Li, Mengyun Chen, Jiamou Liu, Sijie Wang, Shuanggen Jin, Jafet C. M. Andersson, Jonas Olsson, Remco, van de Beek, Hai Victor Habi, Congzheng Han  

**一句话要点**：提出TabGRU混合深度学习架构，用于基于商用微波链路的城市降雨强度估计。

**关键词**：降雨强度估计, 商用微波链路, 深度学习, Transformer, 门控循环单元, 城市监测

## 3 点简述
- 核心问题：传统物理模型在商用微波链路降雨反演中受信号噪声和非线性衰减等现实复杂性限制。
- 方法要点：结合Transformer和双向门控循环单元，捕获长期依赖和局部序列特征，增强位置嵌入和注意力池化。
- 实验或效果：在瑞典哥德堡数据集上验证，优于深度学习基线，R2达0.91-0.96，缓解峰值降雨高估问题。

## 摘要（原文）

> In the face of accelerating global urbanization and the increasing frequency of extreme weather events, highresolution urban rainfall monitoring is crucial for building resilient smart cities. Commercial Microwave Links (CMLs) are an emerging data source with great potential for this task.While traditional rainfall retrieval from CMLs relies on physicsbased models, these often struggle with real-world complexities like signal noise and nonlinear attenuation. To address these limitations, this paper proposes a novel hybrid deep learning architecture based on the Transformer and a Bidirectional Gated Recurrent Unit (BiGRU), which we name TabGRU. This design synergistically captures both long-term dependencies and local sequential features in the CML signal data. The model is further enhanced by a learnable positional embedding and an attention pooling mechanism to improve its dynamic feature extraction and generalization capabilities. The model was validated on a public benchmark dataset from Gothenburg, Sweden (June-September 2015). The evaluation used 12 sub-links from two rain gauges (Torp and Barl) over a test period (August 22-31) covering approximately 10 distinct rainfall events. The proposed TabGRU model demonstrated consistent advantages, outperforming deep learning baselines and achieving high coefficients of determination (R2) at both the Torp site (0.91) and the Barl site (0.96). Furthermore, compared to the physics-based approach, TabGRU maintained higher accuracy and was particularly effective in mitigating the significant overestimation problem observed in the PL model during peak rainfall events. This evaluation confirms that the TabGRU model can effectively overcome the limitations of traditional methods, providing a robust and accurate solution for CML-based urban rainfall monitoring under the tested conditions.

