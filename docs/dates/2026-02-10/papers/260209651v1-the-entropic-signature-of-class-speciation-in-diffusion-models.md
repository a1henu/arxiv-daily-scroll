---
layout: default
title: The Entropic Signature of Class Speciation in Diffusion Models
---

# The Entropic Signature of Class Speciation in Diffusion Models
**arXiv**：[2602.09651v1](https://arxiv.org/abs/2602.09651) · [PDF](https://arxiv.org/pdf/2602.09651.pdf)  
**作者**：Florian Handke, Dejan Stančević, Felix Koulischer, Thomas Demeester, Luca Ambrogioni  

**一句话要点**：提出基于类条件熵的方法以检测扩散模型中的语义结构形成窗口

**关键词**：扩散模型, 类条件熵, 语义结构形成, 信息论分析, 时间局部控制, 统计物理视角

## 3 点简述
- 扩散模型在采样过程中语义结构形成不均匀，存在从模糊到类承诺的窄窗口
- 通过跟踪噪声状态下潜在语义变量的类条件熵，可靠识别这些过渡区域
- 在EDM2-XS和Stable Diffusion 1.5上验证，熵能隔离关键噪声区域并量化引导影响

## 摘要（原文）

> Diffusion models do not recover semantic structure uniformly over time. Instead, samples transition from semantic ambiguity to class commitment within a narrow regime. Recent theoretical work attributes this transition to dynamical instabilities along class-separating directions, but practical methods to detect and exploit these windows in trained models are still limited. We show that tracking the class-conditional entropy of a latent semantic variable given the noisy state provides a reliable signature of these transition regimes. By restricting the entropy to semantic partitions, the entropy can furthermore resolve semantic decisions at different levels of abstraction. We analyze this behavior in high-dimensional Gaussian mixture models and show that the entropy rate concentrates on the same logarithmic time scale as the speciation symmetry-breaking instability previously identified in variance-preserving diffusion. We validate our method on EDM2-XS and Stable Diffusion 1.5, where class-conditional entropy consistently isolates the noise regimes critical for semantic structure formation. Finally, we use our framework to quantify how guidance redistributes semantic information over time. Together, these results connect information-theoretic and statistical physics perspectives on diffusion and provide a principled basis for time-localized control.

