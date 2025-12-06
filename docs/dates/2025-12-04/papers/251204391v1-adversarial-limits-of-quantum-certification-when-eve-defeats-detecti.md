---
layout: default
title: Adversarial Limits of Quantum Certification: When Eve Defeats Detection
---

# Adversarial Limits of Quantum Certification: When Eve Defeats Detection
**arXiv**：[2512.04391v1](https://arxiv.org/abs/2512.04391) · [PDF](https://arxiv.org/pdf/2512.04391.pdf)  
**作者**：Davut Emre Tasar  

**一句话要点**：揭示量子认证的对抗极限：当窃听者通过5%经典混合完全规避检测

**关键词**：量子认证, 对抗极限, 生成对抗网络, 量子密钥分发安全, 分布校准, CHSH测试

## 3 点简述
- 核心问题：量子密钥分发安全依赖认证量子纠缠，但实际面临自适应窃听者攻击，理论证明假设理想条件。
- 方法要点：使用Eve GAN生成与量子不可区分的经典关联，分析混合参数下检测失效，发现分布校准缺陷。
- 实验或效果：在CHSH=2.05处发现相变，硬件验证显示Eve-GAN超越真实量子性能，推荐跨分布校准和对抗测试。

## 摘要（原文）

> Security of quantum key distribution (QKD) relies on certifying that observed correlations arise from genuine quantum entanglement rather than eavesdropper manipulation. Theoretical security proofs assume idealized conditions, practical certification must contend with adaptive adversaries who optimize their attack strategies against detection systems. Established fundamental adversarial limits for quantum certification using Eve GAN, a generative adversarial network trained to produce classical correlations indistinguishable from quantum. Our central finding: when Eve interpolates her classical correlations with quantum data at mixing parameter, all tested detection methods achieve ROC AUC = 0.50, equivalent to random guessing. This means an eavesdropper needs only 5% classical admixture to completely evade detection. Critically, we discover that same distribution calibration a common practice in prior certification studies inflates detection performance by 44 percentage points compared to proper cross distribution evaluation, revealing a systematic flaw that may have led to overestimated security claims. Analysis of Popescu Rohrlich (PR Box) regime identifies a sharp phase transition at CHSH S = 2.05: below this value, no statistical method distinguishes classical from quantum correlations; above it, detection probability increases monotonically. Hardware validation on IBM Quantum demonstrates that Eve-GAN achieves CHSH = 2.736, remarkably exceeding real quantum hardware performance (CHSH = 2.691), illustrating that classical adversaries can outperform noisy quantum systems on standard certification metrics. These results have immediate implications for QKD security: adversaries maintaining 95% quantum fidelity evade all tested detection methods. We provide corrected methodology using cross-distribution calibration and recommend mandatory adversarial testing for quantum security claims.

