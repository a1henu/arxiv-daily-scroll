---
layout: default
title: COP-GEN: Latent Diffusion Transformer for Copernicus Earth Observation Data -- Generation Stochastic by Design
---

# COP-GEN: Latent Diffusion Transformer for Copernicus Earth Observation Data -- Generation Stochastic by Design
**arXiv**：[2603.03239v1](https://arxiv.org/abs/2603.03239) · [PDF](https://arxiv.org/pdf/2603.03239.pdf)  
**作者**：Miguel Espinosa, Eva Gmelich Meijling, Valerio Marsocci, Elliot J. Crowley, Mikolaj Czerkawski  

**一句话要点**：提出COP-GEN以解决地球观测多模态数据生成中的不确定性问题

**关键词**：地球观测数据生成, 潜在扩散变换器, 多模态学习, 条件生成, 不确定性建模

## 3 点简述
- 核心问题：多模态地球观测数据间关系非单射，确定性模型易坍缩为条件均值，无法表示不确定性。
- 方法要点：采用多模态潜在扩散变换器，将跨模态映射参数化为条件分布，支持任意到任意条件生成。
- 实验或效果：在大规模全球数据集上生成多样且物理一致的样本，保持高保真度，并自适应输出不确定性。

## 摘要（原文）

> Earth observation applications increasingly rely on data from multiple sensors, including optical, radar, elevation, and land-cover products. Relationships between these modalities are fundamental for data integration but are inherently non-injective: identical conditioning information can correspond to multiple physically plausible observations. Thus, such conditional mappings should be parametrised as data distributions. As a result, deterministic models tend to collapse toward conditional means and fail to represent the uncertainty and variability required for tasks such as data completion and cross-sensor translation. We introduce COP-GEN, a multimodal latent diffusion transformer that models the joint distribution of heterogeneous Earth Observation modalities at their native spatial resolutions. By parameterising cross-modal mappings as conditional distributions, COP-GEN enables flexible any-to-any conditional generation, including zero-shot modality translation, spectral band infilling, and generation under partial or missing inputs, without task-specific retraining. Experiments on a large-scale global multimodal dataset show that COP-GEN generates diverse yet physically consistent realisations while maintaining strong peak fidelity across optical, radar, and elevation modalities. Qualitative and quantitative analyses demonstrate that the model captures meaningful cross-modal structure and systematically adapts its output uncertainty as conditioning information increases. These results highlight the practical importance of stochastic generative modeling for Earth observation and motivate evaluation protocols that move beyond single-reference, pointwise metrics. Website: https:// miquel-espinosa.github.io/cop-gen

