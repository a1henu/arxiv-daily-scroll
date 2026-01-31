---
layout: default
title: Position: Certifiable State Integrity in Cyber-Physical Systems -- Why Modular Sovereignty Solves the Plasticity-Stability Paradox
---

# Position: Certifiable State Integrity in Cyber-Physical Systems -- Why Modular Sovereignty Solves the Plasticity-Stability Paradox
**arXiv**：[2601.21249v1](https://arxiv.org/abs/2601.21249) · [PDF](https://arxiv.org/pdf/2601.21249.pdf)  
**作者**：Enzo Nicolás Spotorno, Antônio Augusto Medeiros Fröhlich  

**一句话要点**：提出模块化主权范式以解决安全关键信息物理系统中的可塑性-稳定性悖论

**关键词**：信息物理系统, 可塑性-稳定性悖论, 模块化主权, 不确定性感知, 状态完整性认证

## 3 点简述
- 核心问题：全局参数更新导致灾难性遗忘和频谱偏差，阻碍安全标准验证
- 方法要点：采用冻结的特定机制专家库，通过不确定性感知混合实现快速适应
- 实验或效果：未知

## 摘要（原文）

> The machine learning community has achieved remarkable success with universal foundation models for time-series and physical dynamics, largely overcoming earlier approximation barriers in smooth or slowly varying regimes through scale and specialized architectures. However, deploying these monolithic models in safety-critical Cyber-Physical Systems (CPS), governed by non-stationary lifecycle dynamics and strict reliability requirements, reveals persistent challenges. Recent evidence shows that fine-tuning time-series foundation models induces catastrophic forgetting, degrading performance on prior regimes. Standard models continue to exhibit residual spectral bias, smoothing high-frequency discontinuities characteristic of incipient faults, while their opacity hinders formal verification and traceability demanded by safety standards (e.g., ISO 26262, IEC 61508). This position paper argues that the plasticity-stability paradox cannot be fully resolved by global parameter updates (whether via offline fine-tuning or online adaptation). Instead, we advocate a Modular Sovereignty paradigm: a library of compact, frozen regime-specific specialists combined via uncertainty-aware blending, which we term "HYDRA" (Hierarchical uncertaintY-aware Dynamics for Rapidly-Adapting systems). This paradigm ensures regime-conditional validity, rigorous disentanglement of aleatoric and epistemic uncertainties, and modular auditability, offering a certifiable path for robust state integrity across the CPS lifecycle.

