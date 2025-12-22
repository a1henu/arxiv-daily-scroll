---
layout: default
title: Timely Information Updating for Mobile Devices Without and With ML Advice
---

# Timely Information Updating for Mobile Devices Without and With ML Advice
**arXiv**：[2512.17381v1](https://arxiv.org/abs/2512.17381) · [PDF](https://arxiv.org/pdf/2512.17381.pdf)  
**作者**：Yu-Pin Hsu, Yi-Hsuan Tseng  

**一句话要点**：提出在线算法与ML增强算法，优化移动设备信息更新的及时性与成本权衡

**关键词**：信息更新系统, 在线算法, 竞争分析, 机器学习建议, 移动设备, 对抗环境

## 3 点简述
- 研究移动设备监控物理过程时，信息及时性与更新成本之间的基本权衡问题
- 设计在线算法，在多种不确定性下渐近达到最优竞争比，并引入ML建议实现一致性-鲁棒性最优权衡
- 通过对抗环境下的广泛仿真验证理论结果，显示算法对ML建议的阈值响应特性

## 摘要（原文）

> This paper investigates an information update system in which a mobile device monitors a physical process and sends status updates to an access point (AP). A fundamental trade-off arises between the timeliness of the information maintained at the AP and the update cost incurred at the device. To address this trade-off, we propose an online algorithm that determines when to transmit updates using only available observations. The proposed algorithm asymptotically achieves the optimal competitive ratio against an adversary that can simultaneously manipulate multiple sources of uncertainty, including the operation duration, the information staleness, the update cost, and the availability of update opportunities. Furthermore, by incorporating machine learning (ML) advice of unknown reliability into the design, we develop an ML-augmented algorithm that asymptotically attains the optimal consistency-robustness trade-off, even when the adversary can additionally corrupt the ML advice. The optimal competitive ratio scales linearly with the range of update costs, but is unaffected by other uncertainties. Moreover, an optimal competitive online algorithm exhibits a threshold-like response to the ML advice: it either fully trusts or completely ignores the ML advice, as partially trusting the advice cannot improve the consistency without severely degrading the robustness. Extensive simulations in stochastic settings further validate the theoretical findings in the adversarial environment.

