---
layout: default
title: PointCoT: A Multi-modal Benchmark for Explicit 3D Geometric Reasoning
---

# PointCoT: A Multi-modal Benchmark for Explicit 3D Geometric Reasoning
**arXiv**：[2602.23945v1](https://arxiv.org/abs/2602.23945) · [PDF](https://arxiv.org/pdf/2602.23945.pdf)  
**作者**：Dongxu Zhang, Yiding Sun, Pengcheng Li, Yumou Liu, Hongqiang Lin, Haoran Xu, Xiaoxuan Mu, Liang Lin, Wenbiao Yan, Ning Yang, Chaowei Fang, Juanjuan Zhao, Jihua Zhu, Conghui He, Cheng Tan  

**一句话要点**：提出PointCoT框架，通过显式思维链推理解决多模态大语言模型在3D点云理解中的几何幻觉问题。

**关键词**：3D点云理解, 多模态大语言模型, 显式思维链推理, 几何幻觉, 指令调优基准

## 3 点简述
- 当前多模态大语言模型在3D点云理解中面临几何幻觉挑战，常因隐式映射而忽略精确结构细节。
- PointCoT采用“观察、思考、回答”范式，通过双流多模态架构结合语义外观与几何真值，监督模型生成几何基础推理。
- 基于Point-Reason-Instruct基准的实验显示，PointCoT在复杂推理任务上达到先进性能。

## 摘要（原文）

> While Multimodal Large Language Models (MLLMs) demonstrate proficiency in 2D scenes, extending their perceptual intelligence to 3D point cloud understanding remains a significant challenge. Current approaches focus primarily on aligning 3D features with pre-trained models. However, they typically treat geometric reasoning as an implicit mapping process. These methods bypass intermediate logical steps and consequently suffer from geometric hallucinations. They confidently generate plausible responses that fail to ground in precise structural details. To bridge this gap, we present PointCoT, a novel framework that empowers MLLMs with explicit Chain-of-Thought (CoT) reasoning for 3D data. We advocate for a \textit{Look, Think, then Answer} paradigm. In this approach, the model is supervised to generate geometry-grounded rationales before predicting final answers. To facilitate this, we construct Point-Reason-Instruct, a large-scale benchmark comprising $\sim$86k instruction-tuning samples with hierarchical CoT annotations. By leveraging a dual-stream multi-modal architecture, our method synergizes semantic appearance with geometric truth. Extensive experiments demonstrate that PointCoT achieves state-of-the-art performance on complex reasoning tasks.

