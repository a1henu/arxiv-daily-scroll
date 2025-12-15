---
layout: default
title: AutoRefiner: Improving Autoregressive Video Diffusion Models via Reflective Refinement Over the Stochastic Sampling Path
---

# AutoRefiner: Improving Autoregressive Video Diffusion Models via Reflective Refinement Over the Stochastic Sampling Path
**arXiv**：[2512.11203v1](https://arxiv.org/abs/2512.11203) · [PDF](https://arxiv.org/pdf/2512.11203.pdf)  
**作者**：Zhengyang Yu, Akio Hayakawa, Masato Ishii, Qingtao Yu, Takashi Shibuya, Jing Zhang, Yuki Mitsufuji  

**一句话要点**：提出AutoRefiner以改进自回归视频扩散模型的样本保真度

**关键词**：自回归视频扩散模型, 噪声精炼, 推理优化, 样本保真度, KV缓存

## 3 点简述
- 自回归视频扩散模型样本保真度不足，推理时对齐方法计算成本高
- AutoRefiner通过路径噪声精炼和反射KV缓存，在单次前向传递中调制噪声
- 实验显示AutoRefiner作为高效插件，有效提升样本保真度

## 摘要（原文）

> Autoregressive video diffusion models (AR-VDMs) show strong promise as scalable alternatives to bidirectional VDMs, enabling real-time and interactive applications. Yet there remains room for improvement in their sample fidelity. A promising solution is inference-time alignment, which optimizes the noise space to improve sample fidelity without updating model parameters. Yet, optimization- or search-based methods are computationally impractical for AR-VDMs. Recent text-to-image (T2I) works address this via feedforward noise refiners that modulate sampled noises in a single forward pass. Can such noise refiners be extended to AR-VDMs? We identify the failure of naively extending T2I noise refiners to AR-VDMs and propose AutoRefiner-a noise refiner tailored for AR-VDMs, with two key designs: pathwise noise refinement and a reflective KV-cache. Experiments demonstrate that AutoRefiner serves as an efficient plug-in for AR-VDMs, effectively enhancing sample fidelity by refining noise along stochastic denoising paths.

