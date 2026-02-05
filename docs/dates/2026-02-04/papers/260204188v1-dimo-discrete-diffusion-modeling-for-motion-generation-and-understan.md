---
layout: default
title: DiMo: Discrete Diffusion Modeling for Motion Generation and Understanding
---

# DiMo: Discrete Diffusion Modeling for Motion Generation and Understanding
**arXiv**：[2602.04188v1](https://arxiv.org/abs/2602.04188) · [PDF](https://arxiv.org/pdf/2602.04188.pdf)  
**作者**：Ning Zhang, Zhengyu Li, Kwong Weng Loh, Mingxi Xu, Qi Wang, Zhengyu Wen, Xiaoyu He, Wei Zhao, Kehong Gong, Mingyuan Zhang  

**一句话要点**：提出DiMo离散扩散框架，统一文本-运动双向理解与生成，支持质量-延迟权衡。

**关键词**：运动生成, 离散扩散模型, 文本-运动对齐, 残差向量量化, 双向理解, 掩码建模

## 3 点简述
- 核心问题：现有掩码建模方法主要关注文本到运动，缺乏双向理解和统一框架。
- 方法要点：采用离散扩散迭代掩码令牌精炼，结合残差向量量化和组相对策略优化提升性能。
- 实验或效果：在HumanML3D和KIT-ML数据集上展示强运动质量和竞争性双向理解，支持无文本运动补全等任务。

## 摘要（原文）

> Prior masked modeling motion generation methods predominantly study text-to-motion. We present DiMo, a discrete diffusion-style framework, which extends masked modeling to bidirectional text--motion understanding and generation. Unlike GPT-style autoregressive approaches that tokenize motion and decode sequentially, DiMo performs iterative masked token refinement, unifying Text-to-Motion (T2M), Motion-to-Text (M2T), and text-free Motion-to-Motion (M2M) within a single model. This decoding paradigm naturally enables a quality-latency trade-off at inference via the number of refinement steps.We further improve motion token fidelity with residual vector quantization (RVQ) and enhance alignment and controllability with Group Relative Policy Optimization (GRPO). Experiments on HumanML3D and KIT-ML show strong motion quality and competitive bidirectional understanding under a unified framework. In addition, we demonstrate model ability in text-free motion completion, text-guided motion prediction and motion caption correction without architectural change.Additional qualitative results are available on our project page: https://animotionlab.github.io/DiMo/.

