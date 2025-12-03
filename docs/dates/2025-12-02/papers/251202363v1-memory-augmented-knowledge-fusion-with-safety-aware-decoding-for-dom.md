---
layout: default
title: Memory-Augmented Knowledge Fusion with Safety-Aware Decoding for Domain-Adaptive Question Answering
---

# Memory-Augmented Knowledge Fusion with Safety-Aware Decoding for Domain-Adaptive Question Answering
**arXiv**：[2512.02363v1](https://arxiv.org/abs/2512.02363) · [PDF](https://arxiv.org/pdf/2512.02363.pdf)  
**作者**：Lei Fu, Xiang Chen, Kaige Gao Xinyue Huang, Kejian Tong  

**一句话要点**：提出KARMA框架以解决服务领域问答中知识融合与安全输出的挑战

**关键词**：领域自适应问答, 知识融合, 安全解码, 记忆增强, 双编码器架构

## 3 点简述
- 核心问题：服务领域问答系统在整合异构知识源时面临事实一致性和安全性的挑战
- 方法要点：采用双编码器融合知识、门控记忆单元动态调节、安全感知解码器控制输出
- 实验或效果：在专有数据集上验证，KARMA在答案质量和安全性方面优于基线模型

## 摘要（原文）

> Domain-specific question answering (QA) systems for services face unique challenges in integrating heterogeneous knowledge sources while ensuring both accuracy and safety. Existing large language models often struggle with factual consistency and context alignment in sensitive domains such as healthcare policies and government welfare. In this work, we introduce Knowledge-Aware Reasoning and Memory-Augmented Adaptation (KARMA), a novel framework designed to enhance QA performance in care scenarios. KARMA incorporates a dual-encoder architecture to fuse structured and unstructured knowledge sources, a gated memory unit to dynamically regulate external knowledge integration, and a safety-aware controllable decoder that mitigates unsafe outputs using safety classification and guided generation techniques. Extensive experiments on a proprietary QA dataset demonstrate that KARMA outperforms strong baselines in both answer quality and safety. This study offers a comprehensive solution for building trustworthy and adaptive QA systems in service contexts.

