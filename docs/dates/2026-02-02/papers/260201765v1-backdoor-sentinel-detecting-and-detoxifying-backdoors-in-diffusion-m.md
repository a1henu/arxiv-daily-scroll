---
layout: default
title: Backdoor Sentinel: Detecting and Detoxifying Backdoors in Diffusion Models via Temporal Noise Consistency
---

# Backdoor Sentinel: Detecting and Detoxifying Backdoors in Diffusion Models via Temporal Noise Consistency
**arXiv**：[2602.01765v1](https://arxiv.org/abs/2602.01765) · [PDF](https://arxiv.org/pdf/2602.01765.pdf)  
**作者**：Bingzheng Wang, Xiaoyan Gu, Hongbo Xu, Hongcheng Li, Zimo Yu, Jiang Zhou, Weiping Wang  

**一句话要点**：提出TNC-Defense框架，通过时序噪声一致性检测和净化扩散模型中的后门攻击。

**关键词**：扩散模型, 后门检测, 时序噪声一致性, 灰盒防御, 模型净化

## 3 点简述
- 核心问题：扩散模型在审计场景中面临后门攻击，现有方法因无法访问参数或影响生成质量而受限。
- 方法要点：利用时序噪声不一致性现象，设计灰盒检测模块定位异常时间步，并构建触发无关的净化模块。
- 实验或效果：在五种攻击场景下，检测准确率平均提升11%，净化后触发样本无效率达98.5%，生成质量仅轻微下降。

## 摘要（原文）

> Diffusion models have been widely deployed in AIGC services; however, their reliance on opaque training data and procedures exposes a broad attack surface for backdoor injection. In practical auditing scenarios, due to the protection of intellectual property and commercial confidentiality, auditors are typically unable to access model parameters, rendering existing white-box or query-intensive detection methods impractical. More importantly, even after the backdoor is detected, existing detoxification approaches are often trapped in a dilemma between detoxification effectiveness and generation quality.
>   In this work, we identify a previously unreported phenomenon called temporal noise unconsistency, where the noise predictions between adjacent diffusion timesteps is disrupted in specific temporal segments when the input is triggered, while remaining stable under clean inputs. Leveraging this finding, we propose Temporal Noise Consistency Defense (TNC-Defense), a unified framework for backdoor detection and detoxification. The framework first uses the adjacent timestep noise consistency to design a gray-box detection module, for identifying and locating anomalous diffusion timesteps. Furthermore, the framework uses the identified anomalous timesteps to construct a trigger-agnostic, timestep-aware detoxification module, which directly corrects the backdoor generation path. This effectively suppresses backdoor behavior while significantly reducing detoxification costs.
>   We evaluate the proposed method under five representative backdoor attack scenarios and compare it with state-of-the-art defenses. The results show that TNC-Defense improves the average detection accuracy by $11\%$ with negligible additional overhead, and invalidates an average of $98.5\%$ of triggered samples with only a mild degradation in generation quality.

