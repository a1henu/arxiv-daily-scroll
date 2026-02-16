---
layout: default
title: Towards reconstructing experimental sparse-view X-ray CT data with diffusion models
---

# Towards reconstructing experimental sparse-view X-ray CT data with diffusion models
**arXiv**：[2602.12755v1](https://arxiv.org/abs/2602.12755) · [PDF](https://arxiv.org/pdf/2602.12755.pdf)  
**作者**：Nelas J. Thomsen, Xinyuan Wang, Felix Lucka, Ezgi Demircan-Tureyen  

**一句话要点**：研究扩散模型在稀疏视图X射线CT实验数据重建中的应用，分析领域偏移与正向模型失配的影响。

**关键词**：稀疏视图CT重建, 扩散模型先验, 领域偏移分析, 正向模型失配, 分解扩散采样, 退火似然调度

## 3 点简述
- 核心问题：扩散模型作为先验在稀疏视图CT逆问题中的应用，需解决合成与实验数据间的领域偏移和正向模型失配问题。
- 方法要点：使用分解扩散采样方案，训练不同领域偏移程度的扩散先验，并采用退火似然调度缓解失配。
- 实验或效果：实验表明，领域偏移影响复杂，多样先验优于匹配但狭窄先验；正向模型失配导致伪影，但可通过调度减轻并提高计算效率。

## 摘要（原文）

> Diffusion-based image generators are promising priors for ill-posed inverse problems like sparse-view X-ray Computed Tomography (CT). As most studies consider synthetic data, it is not clear whether training data mismatch (``domain shift'') or forward model mismatch complicate their successful application to experimental data. We measured CT data from a physical phantom resembling the synthetic Shepp-Logan phantom and trained diffusion priors on synthetic image data sets with different degrees of domain shift towards it. Then, we employed the priors in a Decomposed Diffusion Sampling scheme on sparse-view CT data sets with increasing difficulty leading to the experimental data. Our results reveal that domain shift plays a nuanced role: while severe mismatch causes model collapse and hallucinations, diverse priors outperform well-matched but narrow priors. Forward model mismatch pulls the image samples away from the prior manifold, which causes artifacts but can be mitigated with annealed likelihood schedules that also increase computational efficiency. Overall, we demonstrate that performance gains do not immediately translate from synthetic to experimental data, and future development must validate against real-world benchmarks.

