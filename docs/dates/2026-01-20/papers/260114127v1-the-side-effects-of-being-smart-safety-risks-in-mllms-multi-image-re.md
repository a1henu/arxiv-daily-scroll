---
layout: default
title: The Side Effects of Being Smart: Safety Risks in MLLMs' Multi-Image Reasoning
---

# The Side Effects of Being Smart: Safety Risks in MLLMs' Multi-Image Reasoning
**arXiv**：[2601.14127v1](https://arxiv.org/abs/2601.14127) · [PDF](https://arxiv.org/pdf/2601.14127.pdf)  
**作者**：Renmiao Chen, Yida Lu, Shiyao Cui, Xuan Ouyang, Victor Shea-Jay Huang, Shumin Zhang, Chengwei Pan, Han Qiu, Minlie Huang  

**一句话要点**：提出MIR-SafetyBench以评估多模态大语言模型在多图像推理中的安全风险

**关键词**：多模态大语言模型, 多图像推理, 安全基准, 注意力熵, 安全风险, 评估框架

## 3 点简述
- 核心问题：多模态大语言模型在多图像推理能力增强时可能引发新的安全风险
- 方法要点：构建首个多图像推理安全基准MIR-SafetyBench，包含9类关系和2676个实例
- 实验或效果：评估19个模型发现推理能力越强越易受攻击，不安全响应平均注意力熵较低

## 摘要（原文）

> As Multimodal Large Language Models (MLLMs) acquire stronger reasoning capabilities to handle complex, multi-image instructions, this advancement may pose new safety risks. We study this problem by introducing MIR-SafetyBench, the first benchmark focused on multi-image reasoning safety, which consists of 2,676 instances across a taxonomy of 9 multi-image relations. Our extensive evaluations on 19 MLLMs reveal a troubling trend: models with more advanced multi-image reasoning can be more vulnerable on MIR-SafetyBench. Beyond attack success rates, we find that many responses labeled as safe are superficial, often driven by misunderstanding or evasive, non-committal replies. We further observe that unsafe generations exhibit lower attention entropy than safe ones on average. This internal signature suggests a possible risk that models may over-focus on task solving while neglecting safety constraints. Our code and data are available at https://github.com/thu-coai/MIR-SafetyBench.

