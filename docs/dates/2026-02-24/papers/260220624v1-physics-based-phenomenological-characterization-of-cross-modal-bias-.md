---
layout: default
title: Physics-based phenomenological characterization of cross-modal bias in multimodal models
---

# Physics-based phenomenological characterization of cross-modal bias in multimodal models
**arXiv**：[2602.20624v1](https://arxiv.org/abs/2602.20624) · [PDF](https://arxiv.org/pdf/2602.20624.pdf)  
**作者**：Hyeongmo Kim, Sohyun Kang, Yerin Choi, Seungyeon Ji, Junhyuk Woo, Hyunsuk Chung, Soyeon Caren Han, Kyungreem Han  

**一句话要点**：提出基于物理的替代模型分析多模态大语言模型中的跨模态偏见动态

**关键词**：多模态大语言模型, 算法公平性, 跨模态偏见, 现象学可解释性, 物理替代模型, Transformer动态分析

## 3 点简述
- 核心问题：多模态交互中的隐蔽扭曲可能导致系统性偏见，传统分析方法未能完全捕捉
- 方法要点：开发基于物理的替代模型描述Transformer动态，采用现象学可解释方法
- 实验效果：通过扰动分析和混沌时间序列预测，揭示多模态输入可能强化模态主导而非缓解

## 摘要（原文）

> The term 'algorithmic fairness' is used to evaluate whether AI models operate fairly in both comparative (where fairness is understood as formal equality, such as "treat like cases as like") and non-comparative (where unfairness arises from the model's inaccuracy, arbitrariness, or inscrutability) contexts. Recent advances in multimodal large language models (MLLMs) are breaking new ground in multimodal understanding, reasoning, and generation; however, we argue that inconspicuous distortions arising from complex multimodal interaction dynamics can lead to systematic bias. The purpose of this position paper is twofold: first, it is intended to acquaint AI researchers with phenomenological explainable approaches that rely on the physical entities that the machine experiences during training/inference, as opposed to the traditional cognitivist symbolic account or metaphysical approaches; second, it is to state that this phenomenological doctrine will be practically useful for tackling algorithmic fairness issues in MLLMs. We develop a surrogate physics-based model that describes transformer dynamics (i.e., semantic network structure and self-/cross-attention) to analyze the dynamics of cross-modal bias in MLLM, which are not fully captured by conventional embedding- or representation-level analyses. We support this position through multi-input diagnostic experiments: 1) perturbation-based analyses of emotion classification using Qwen2.5-Omni and Gemma 3n, and 2) dynamical analysis of Lorenz chaotic time-series prediction through the physical surrogate. Across two architecturally distinct MLLMs, we show that multimodal inputs can reinforce modality dominance rather than mitigate it, as revealed by structured error-attractor patterns under systematic label perturbation, complemented by dynamical analysis.

