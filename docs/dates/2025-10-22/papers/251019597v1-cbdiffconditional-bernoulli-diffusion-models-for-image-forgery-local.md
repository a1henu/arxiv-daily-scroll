---
layout: default
title: CBDiff:Conditional Bernoulli Diffusion Models for Image Forgery Localization
---

# CBDiff:Conditional Bernoulli Diffusion Models for Image Forgery Localization
**arXiv**：[2510.19597v1](https://arxiv.org/abs/2510.19597) · [PDF](https://arxiv.org/pdf/2510.19597.pdf)  
**作者**：Zhou Lei, Pan Gang, Wang Jiahao, Sun Di  

**一句话要点**：提出条件伯努利扩散模型以解决图像伪造定位中的不确定性问题

**关键词**：图像伪造定位, 扩散模型, 伯努利噪声, 时间步交叉注意力, 像素级检测, 不确定性建模

## 3 点简述
- 核心问题：现有方法生成单一确定性定位图，缺乏精度和可靠性，难以满足高要求应用。
- 方法要点：引入条件伯努利扩散模型，生成多样伪造定位图，并融入伯努利噪声和时间步交叉注意力。
- 实验或效果：在八个公开数据集上实验，性能显著优于现有先进方法，具有实际部署潜力。

## 摘要（原文）

> Image Forgery Localization (IFL) is a crucial task in image forensics, aimed
> at accurately identifying manipulated or tampered regions within an image at
> the pixel level. Existing methods typically generate a single deterministic
> localization map, which often lacks the precision and reliability required for
> high-stakes applications such as forensic analysis and security surveillance.
> To enhance the credibility of predictions and mitigate the risk of errors, we
> introduce an advanced Conditional Bernoulli Diffusion Model (CBDiff). Given a
> forged image, CBDiff generates multiple diverse and plausible localization
> maps, thereby offering a richer and more comprehensive representation of the
> forgery distribution. This approach addresses the uncertainty and variability
> inherent in tampered regions. Furthermore, CBDiff innovatively incorporates
> Bernoulli noise into the diffusion process to more faithfully reflect the
> inherent binary and sparse properties of forgery masks. Additionally, CBDiff
> introduces a Time-Step Cross-Attention (TSCAttention), which is specifically
> designed to leverage semantic feature guidance with temporal steps to improve
> manipulation detection. Extensive experiments on eight publicly benchmark
> datasets demonstrate that CBDiff significantly outperforms existing
> state-of-the-art methods, highlighting its strong potential for real-world
> deployment.

