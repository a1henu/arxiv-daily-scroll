---
layout: default
title: Semantically Conditioned Diffusion Models for Cerebral DSA Synthesis
---

# Semantically Conditioned Diffusion Models for Cerebral DSA Synthesis
**arXiv**：[2602.11703v1](https://arxiv.org/abs/2602.11703) · [PDF](https://arxiv.org/pdf/2602.11703.pdf)  
**作者**：Qiwen Xu, David Rügamer, Holger Wenz, Johann Fontana, Nora Meggyeshazi, Andreas Bender, Máté E. Maros  

**一句话要点**：提出语义条件潜在扩散模型以合成脑部数字减影血管造影图像，用于算法开发与训练。

**关键词**：数字减影血管造影, 潜在扩散模型, 语义控制, 医学图像合成, 脑血管疾病

## 3 点简述
- 核心问题：脑部DSA图像采集成本高且侵入性强，限制数据共享与大规模收集。
- 方法要点：基于文本嵌入控制解剖循环和C臂位置，训练条件潜在扩散模型生成合成图像。
- 实验或效果：专家评估显示合成图像临床真实感高，FID分数低，适用于下游应用。

## 摘要（原文）

> Digital subtraction angiography (DSA) plays a central role in the diagnosis and treatment of cerebrovascular disease, yet its invasive nature and high acquisition cost severely limit large-scale data collection and public data sharing. Therefore, we developed a semantically conditioned latent diffusion model (LDM) that synthesizes arterial-phase cerebral DSA frames under explicit control of anatomical circulation (anterior vs.\ posterior) and canonical C-arm positions. We curated a large single-centre DSA dataset of 99,349 frames and trained a conditional LDM using text embeddings that encoded anatomy and acquisition geometry. To assess clinical realism, four medical experts, including two neuroradiologists, one neurosurgeon, and one internal medicine expert, systematically rated 400 synthetic DSA images using a 5-grade Likert scale for evaluating proximal large, medium, and small peripheral vessels. The generated images achieved image-wise overall Likert scores ranging from 3.1 to 3.3, with high inter-rater reliability (ICC(2,k) = 0.80--0.87). Distributional similarity to real DSA frames was supported by a low median Fréchet inception distance (FID) of 15.27. Our results indicate that semantically controlled LDMs can produce realistic synthetic DSAs suitable for downstream algorithm development, research, and training.

