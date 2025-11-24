---
layout: default
title: OmniGround: A Comprehensive Spatio-Temporal Grounding Benchmark for Real-World Complex Scenarios
---

# OmniGround: A Comprehensive Spatio-Temporal Grounding Benchmark for Real-World Complex Scenarios
**arXiv**：[2511.16937v1](https://arxiv.org/abs/2511.16937) · [PDF](https://arxiv.org/pdf/2511.16937.pdf)  
**作者**：Hong Gao, Jingyu Wu, Xiangkai Xu, Kangni Xie, Yunchen Zhang, Bin Zhong, Xurui Gao, Min-Ling Zhang  

**一句话要点**：提出OmniGround基准和PG-TAF框架以解决复杂场景时空视频定位问题

**关键词**：时空视频定位, 基准构建, 训练免费框架, 多模态语言模型, 复杂查询处理

## 3 点简述
- 核心问题：现有STVG模型在真实复杂场景中表现不佳，存在类别偏见和推理简化问题
- 方法要点：引入OmniGround基准和PG-TAF训练免费框架，分解时空定位任务
- 实验或效果：PG-TAF在OmniGround上m_tIoU和m_vIoU分别提升25.6%和35.6%

## 摘要（原文）

> Spatio-Temporal Video Grounding (STVG) aims to localize target objects in videos based on natural language descriptions. Despite recent advances in Multimodal Large Language Models, a significant gap remains between current models and real-world demands involving diverse objects and complex queries. We attribute this to limited benchmark scope, causing models to exhibit category bias, oversimplified reasoning, and poor linguistic robustness. To address these limitations, we introduce OmniGround, a comprehensive benchmark with 3,475 videos spanning 81 categories and complex real-world queries. We propose the Forward-Backward-Refinement annotation pipeline that combines multi-directional tracking with intelligent error correction for high-quality labels. We further introduce DeepSTG, a systematic evaluation framework quantifying dataset quality across four complementary dimensions beyond superficial statistics. Evaluations reveal performance average drop of 10.4% on complex real-world scenes, particularly with small/occluded objects and intricate spatial relations. Motivated by these, we propose PG-TAF, a training-free two-stage framework decomposing STVG into high-level temporal grounding and fine-grained spatio-temporal propagation. Experiments demonstrate PG-TAF achieves 25.6% and 35.6% improvements in m\_tIoU and m\_vIoU on OmniGround with consistent gains across four benchmarks.

