---
layout: default
title: Lossless Copyright Protection via Intrinsic Model Fingerprinting
---

# Lossless Copyright Protection via Intrinsic Model Fingerprinting
**arXiv**：[2601.21252v1](https://arxiv.org/abs/2601.21252) · [PDF](https://arxiv.org/pdf/2601.21252.pdf)  
**作者**：Lingxiao Chen, Liqin Wang, Wei Lu, Xiangyang Luo  

**一句话要点**：提出TrajPrint框架，通过提取确定性生成中的流形指纹，实现黑盒API场景下的无损版权验证。

**关键词**：扩散模型, 版权保护, 模型指纹, 黑盒验证, 无损水印, 流形学习

## 3 点简述
- 核心问题：扩散模型作为高价值知识产权易受未授权复制，现有方法或损害性能或与黑盒API不兼容。
- 方法要点：利用水印图像锚定并回溯轨迹起源，通过双端锚定联合优化合成特定指纹噪声，实现无损指纹提取与验证。
- 实验或效果：在广泛实验中，TrajPrint在黑盒API场景下实现无损验证，对模型修改具有优越鲁棒性。

## 摘要（原文）

> The exceptional performance of diffusion models establishes them as high-value intellectual property but exposes them to unauthorized replication. Existing protection methods either modify the model to embed watermarks, which impairs performance, or extract model fingerprints by manipulating the denoising process, rendering them incompatible with black-box APIs. In this paper, we propose TrajPrint, a completely lossless and training-free framework that verifies model copyright by extracting unique manifold fingerprints formed during deterministic generation. Specifically, we first utilize a watermarked image as an anchor and exactly trace the path back to its trajectory origin, effectively locking the model fingerprint mapped by this path. Subsequently, we implement a joint optimization strategy that employs dual-end anchoring to synthesize a specific fingerprint noise, which strictly adheres to the target manifold for robust watermark recovery. As input, it enables the protected target model to recover the watermarked image, while failing on non-target models. Finally, we achieved verification via atomic inference and statistical hypothesis testing. Extensive experiments demonstrate that TrajPrint achieves lossless verification in black-box API scenarios with superior robustness against model modifications.

