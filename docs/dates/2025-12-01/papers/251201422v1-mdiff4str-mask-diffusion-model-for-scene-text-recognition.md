---
layout: default
title: MDiff4STR: Mask Diffusion Model for Scene Text Recognition
---

# MDiff4STR: Mask Diffusion Model for Scene Text Recognition
**arXiv**：[2512.01422v1](https://arxiv.org/abs/2512.01422) · [PDF](https://arxiv.org/pdf/2512.01422.pdf)  
**作者**：Yongkun Du, Miaomiao Zhao, Songlin Fan, Zhineng Chen, Caiyan Jia, Yu-Gang Jiang  

**一句话要点**：提出MDiff4STR，通过改进噪声策略解决掩码扩散模型在场景文本识别中的性能差距。

**关键词**：场景文本识别, 掩码扩散模型, 噪声策略优化, 令牌替换噪声, 高效推理

## 3 点简述
- 核心问题：掩码扩散模型在场景文本识别中训练与推理噪声不匹配及预测过度自信。
- 方法要点：设计六种噪声策略对齐训练推理，引入令牌替换噪声机制修正错误预测。
- 实验或效果：在多种场景文本基准测试中超越自回归模型，仅需三步去噪保持高效推理。

## 摘要（原文）

> Mask Diffusion Models (MDMs) have recently emerged as a promising alternative to auto-regressive models (ARMs) for vision-language tasks, owing to their flexible balance of efficiency and accuracy. In this paper, for the first time, we introduce MDMs into the Scene Text Recognition (STR) task. We show that vanilla MDM lags behind ARMs in terms of accuracy, although it improves recognition efficiency. To bridge this gap, we propose MDiff4STR, a Mask Diffusion model enhanced with two key improvement strategies tailored for STR. Specifically, we identify two key challenges in applying MDMs to STR: noising gap between training and inference, and overconfident predictions during inference. Both significantly hinder the performance of MDMs. To mitigate the first issue, we develop six noising strategies that better align training with inference behavior. For the second, we propose a token-replacement noise mechanism that provides a non-mask noise type, encouraging the model to reconsider and revise overly confident but incorrect predictions. We conduct extensive evaluations of MDiff4STR on both standard and challenging STR benchmarks, covering diverse scenarios including irregular, artistic, occluded, and Chinese text, as well as whether the use of pretraining. Across these settings, MDiff4STR consistently outperforms popular STR models, surpassing state-of-the-art ARMs in accuracy, while maintaining fast inference with only three denoising steps. Code: https://github.com/Topdu/OpenOCR.

