---
layout: default
title: MedXIAOHE: A Comprehensive Recipe for Building Medical MLLMs
---

# MedXIAOHE: A Comprehensive Recipe for Building Medical MLLMs
**arXiv**：[2602.12705v1](https://arxiv.org/abs/2602.12705) · [PDF](https://arxiv.org/pdf/2602.12705.pdf)  
**作者**：Baorong Shi, Bo Cui, Boyuan Jiang, Deli Yu, Fang Qian, Haihua Yang, Huichao Wang, Jiale Chen, Jianfei Pan, Jieqiong Cao, Jinghao Lin, Kai Wu, Lin Yang, Shengsheng Yao, Tao Chen, Xiaojun Xiao, Xiaozhong Ji, Xu Wang, Yijun He, Zhixiong Yang  

**一句话要点**：提出MedXIAOHE医疗多模态大模型，以提升真实临床应用的通用医疗理解与推理能力。

**关键词**：医疗多模态大模型, 实体感知预训练, 医疗推理模式, 工具增强训练, 低幻觉报告生成

## 3 点简述
- 核心问题：解决医疗多模态模型在真实临床应用中知识覆盖不足、长尾差距和推理可靠性低的问题。
- 方法要点：采用实体感知持续预训练框架，结合强化学习和工具增强代理训练，集成用户偏好和证据推理。
- 实验或效果：在多个医疗基准上达到最先进性能，超越领先闭源系统，并实现低幻觉长报告生成。

## 摘要（原文）

> We present MedXIAOHE, a medical vision-language foundation model designed to advance general-purpose medical understanding and reasoning in real-world clinical applications. MedXIAOHE achieves state-of-the-art performance across diverse medical benchmarks and surpasses leading closed-source multimodal systems on multiple capabilities. To achieve this, we propose an entity-aware continual pretraining framework that organizes heterogeneous medical corpora to broaden knowledge coverage and reduce long-tail gaps (e.g., rare diseases). For medical expert-level reasoning and interaction, MedXIAOHE incorporates diverse medical reasoning patterns via reinforcement learning and tool-augmented agentic training, enabling multi-step diagnostic reasoning with verifiable decision traces. To improve reliability in real-world use, MedXIAOHE integrates user-preference rubrics, evidence-grounded reasoning, and low-hallucination long-form report generation, with improved adherence to medical instructions. We release this report to document our practical design choices, scaling insights, and evaluation framework, hoping to inspire further research.

