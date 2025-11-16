---
layout: default
title: LLM-YOLOMS: Large Language Model-based Semantic Interpretation and Fault Diagnosis for Wind Turbine Components
---

# LLM-YOLOMS: Large Language Model-based Semantic Interpretation and Fault Diagnosis for Wind Turbine Components
**arXiv**：[2511.10394v1](https://arxiv.org/abs/2511.10394) · [PDF](https://arxiv.org/pdf/2511.10394.pdf)  
**作者**：Yaru Li, Yanxue Wang, Meng Li, Xinming Li, Jianbo Feng  

**一句话要点**：提出LLM-YOLOMS框架以解决风力涡轮机故障检测语义解释不足问题

**关键词**：风力涡轮机故障诊断, 多尺度目标检测, 语义解释, 大语言模型应用, 维护决策支持

## 3 点简述
- 核心问题：现有故障检测方法依赖视觉识别，输出缺乏语义解释，难以支持维护决策。
- 方法要点：结合YOLOMS多尺度检测与LLM语义推理，通过KV映射模块连接视觉与文本。
- 实验或效果：真实数据集上故障检测准确率90.6%，维护报告准确率89%，提升可解释性。

## 摘要（原文）

> The health condition of wind turbine (WT) components is crucial for ensuring stable and reliable operation. However, existing fault detection methods are largely limited to visual recognition, producing structured outputs that lack semantic interpretability and fail to support maintenance decision-making. To address these limitations, this study proposes an integrated framework that combines YOLOMS with a large language model (LLM) for intelligent fault analysis and diagnosis. Specifically, YOLOMS employs multi-scale detection and sliding-window cropping to enhance fault feature extraction, while a lightweight key-value (KV) mapping module bridges the gap between visual outputs and textual inputs. This module converts YOLOMS detection results into structured textual representations enriched with both qualitative and quantitative attributes. A domain-tuned LLM then performs semantic reasoning to generate interpretable fault analyses and maintenance recommendations. Experiments on real-world datasets demonstrate that the proposed framework achieves a fault detection accuracy of 90.6\% and generates maintenance reports with an average accuracy of 89\%, thereby improving the interpretability of diagnostic results and providing practical decision support for the operation and maintenance of wind turbines.

