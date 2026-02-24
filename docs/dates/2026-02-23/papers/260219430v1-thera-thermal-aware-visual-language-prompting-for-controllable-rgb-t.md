---
layout: default
title: TherA: Thermal-Aware Visual-Language Prompting for Controllable RGB-to-Thermal Infrared Translation
---

# TherA: Thermal-Aware Visual-Language Prompting for Controllable RGB-to-Thermal Infrared Translation
**arXiv**：[2602.19430v1](https://arxiv.org/abs/2602.19430) · [PDF](https://arxiv.org/pdf/2602.19430.pdf)  
**作者**：Dong-Guw Lee, Tai Hyoung Rhee, Hyunsoo Jang, Young-Sik Shin, Ukcheol Shin, Ayoung Kim  

**一句话要点**：提出TherA框架，通过热感知视觉语言提示实现可控的RGB到热红外图像翻译，以解决热物理忽略问题。

**关键词**：热红外图像翻译, 视觉语言模型, 潜在扩散模型, 可控图像合成, 热感知嵌入

## 3 点简述
- 核心问题：RGB到热红外翻译方法常依赖RGB先验，忽略热物理，导致热分布不真实。
- 方法要点：结合TherA-VLM和潜在扩散模型，基于用户提示生成热感知嵌入，实现场景和对象级可控翻译。
- 实验或效果：在基准测试中达到最佳性能，零样本翻译指标平均提升高达33%。

## 摘要（原文）

> Despite the inherent advantages of thermal infrared(TIR) imaging, large-scale data collection and annotation remain a major bottleneck for TIR-based perception. A practical alternative is to synthesize pseudo TIR data via image translation; however, most RGB-to-TIR approaches heavily rely on RGB-centric priors that overlook thermal physics, yielding implausible heat distributions. In this paper, we introduce TherA, a controllable RGB-to-TIR translation framework that produces diverse and thermally plausible images at both scene and object level. TherA couples TherA-VLM with a latent-diffusion-based translator. Given a single RGB image and a user-prompted condition pair, TherA-VLM yields a thermal-aware embedding that encodes scene, object, material, and heat-emission context reflecting the input scene-condition pair. Conditioning the diffusion model on this embedding enables realistic TIR synthesis and fine-grained control across time of day, weather, and object state. Compared to other baselines, TherA achieves state-of-the-art translation performance, demonstrating improved zero-shot translation performance up to 33% increase averaged across all metrics.

