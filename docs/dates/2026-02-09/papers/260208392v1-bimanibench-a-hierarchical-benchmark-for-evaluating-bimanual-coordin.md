---
layout: default
title: BiManiBench: A Hierarchical Benchmark for Evaluating Bimanual Coordination of Multimodal Large Language Models
---

# BiManiBench: A Hierarchical Benchmark for Evaluating Bimanual Coordination of Multimodal Large Language Models
**arXiv**：[2602.08392v1](https://arxiv.org/abs/2602.08392) · [PDF](https://arxiv.org/pdf/2602.08392.pdf)  
**作者**：Xin Wu, Zhixuan Liang, Yue Ma, Mengkang Hu, Zhiyuan Qin, Xiu Li  

**一句话要点**：提出BiManiBench分层基准以评估多模态大语言模型在机器人双手协调任务中的能力

**关键词**：双手协调评估, 多模态大语言模型, 机器人操作基准, 分层评估框架, 空间推理, 动作规划

## 3 点简述
- 现有基准主要针对单臂操作，无法评估双手任务所需的时空协调能力
- 构建三层评估框架：基础空间推理、高层动作规划、低层末端执行器控制
- 分析30多个先进模型发现，模型在双臂空间定位和控制方面存在显著困难

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have significantly advanced embodied AI, and using them to benchmark robotic intelligence has become a pivotal trend. However, existing frameworks remain predominantly confined to single-arm manipulation, failing to capture the spatio-temporal coordination required for bimanual tasks like lifting a heavy pot. To address this, we introduce BiManiBench, a hierarchical benchmark evaluating MLLMs across three tiers: fundamental spatial reasoning, high-level action planning, and low-level end-effector control. Our framework isolates unique bimanual challenges, such as arm reachability and kinematic constraints, thereby distinguishing perceptual hallucinations from planning failures. Analysis of over 30 state-of-the-art models reveals that despite high-level reasoning proficiency, MLLMs struggle with dual-arm spatial grounding and control, frequently resulting in mutual interference and sequencing errors. These findings suggest the current paradigm lacks a deep understanding of mutual kinematic constraints, highlighting the need for future research to focus on inter-arm collision-avoidance and fine-grained temporal sequencing.

