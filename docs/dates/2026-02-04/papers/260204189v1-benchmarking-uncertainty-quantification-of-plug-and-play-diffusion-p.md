---
layout: default
title: Benchmarking Uncertainty Quantification of Plug-and-Play Diffusion Priors for Inverse Problems Solving
---

# Benchmarking Uncertainty Quantification of Plug-and-Play Diffusion Priors for Inverse Problems Solving
**arXiv**：[2602.04189v1](https://arxiv.org/abs/2602.04189) · [PDF](https://arxiv.org/pdf/2602.04189.pdf)  
**作者**：Xiaoyu Qiu, Taewon Yang, Zhanhao Liu, Guanyang Wang, Liyue Shen  

**一句话要点**：提出基准测试以评估即插即用扩散先验在逆问题求解中的不确定性量化

**关键词**：不确定性量化, 即插即用扩散先验, 逆问题求解, 基准测试, 扩散模型, 科学计算

## 3 点简述
- 核心问题：现有评估仅关注单样本点估计精度，忽略逆问题的随机性和不确定性。
- 方法要点：设计玩具模型模拟，系统评估扩散逆求解器的不确定性行为并提出分类。
- 实验或效果：在玩具模拟和真实科学逆问题中验证分类，提供不确定性评估新见解。

## 摘要（原文）

> Plug-and-play diffusion priors (PnPDP) have become a powerful paradigm for solving inverse problems in scientific and engineering domains. Yet, current evaluations of reconstruction quality emphasize point-estimate accuracy metrics on a single sample, which do not reflect the stochastic nature of PnPDP solvers and the intrinsic uncertainty of inverse problems, critical for scientific tasks. This creates a fundamental mismatch: in inverse problems, the desired output is typically a posterior distribution and most PnPDP solvers induce a distribution over reconstructions, but existing benchmarks only evaluate a single reconstruction, ignoring distributional characterization such as uncertainty. To address this gap, we conduct a systematic study to benchmark the uncertainty quantification (UQ) of existing diffusion inverse solvers. Specifically, we design a rigorous toy model simulation to evaluate the uncertainty behavior of various PnPDP solvers, and propose a UQ-driven categorization. Through extensive experiments on toy simulations and diverse real-world scientific inverse problems, we observe uncertainty behaviors consistent with our taxonomy and theoretical justification, providing new insights for evaluating and understanding the uncertainty for PnPDPs.

