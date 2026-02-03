---
layout: default
title: On Stability and Robustness of Diffusion Posterior Sampling for Bayesian Inverse Problems
---

# On Stability and Robustness of Diffusion Posterior Sampling for Bayesian Inverse Problems
**arXiv**：[2602.02045v1](https://arxiv.org/abs/2602.02045) · [PDF](https://arxiv.org/pdf/2602.02045.pdf)  
**作者**：Yiming Yang, Xiaoyuan Cheng, Yi He, Kaiyu Li, Wenxuan Yuan, Zhuo Sun  

**一句话要点**：提出鲁棒扩散后验采样以解决贝叶斯逆问题中似然失配导致的稳定性与鲁棒性问题

**关键词**：扩散模型, 贝叶斯逆问题, 后验采样, 稳定性分析, 鲁棒性优化, 似然失配

## 3 点简述
- 核心问题：扩散模型作为先验用于贝叶斯逆问题时，似然与恢复质量关系不明，且存在鲁棒性不足问题
- 方法要点：通过理论分析稳定性，并提出鲁棒扩散后验采样方法，兼容现有梯度后验采样器
- 实验或效果：在科学逆问题和自然图像任务中验证方法有效，在似然失配下性能提升

## 摘要（原文）

> Diffusion models have recently emerged as powerful learned priors for Bayesian inverse problems (BIPs). Diffusion-based solvers rely on a presumed likelihood for the observations in BIPs to guide the generation process. However, the link between likelihood and recovery quality for BIPs is unclear in previous works. We bridge this gap by characterizing the posterior approximation error and proving the \emph{stability} of the diffusion-based solvers. Meanwhile, an immediate result of our findings on stability demonstrates the lack of robustness in diffusion-based solvers, which remains unexplored. This can degrade performance when the presumed likelihood mismatches the unknown true data generation processes. To address this issue, we propose a simple yet effective solution, \emph{robust diffusion posterior sampling}, which is provably \emph{robust} and compatible with existing gradient-based posterior samplers. Empirical results on scientific inverse problems and natural image tasks validate the effectiveness and robustness of our method, showing consistent performance improvements under challenging likelihood misspecifications.

