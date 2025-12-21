---
layout: default
title: PrivateXR: Defending Privacy Attacks in Extended Reality Through Explainable AI-Guided Differential Privacy
---

# PrivateXR: Defending Privacy Attacks in Extended Reality Through Explainable AI-Guided Differential Privacy
**arXiv**：[2512.16851v1](https://arxiv.org/abs/2512.16851) · [PDF](https://arxiv.org/pdf/2512.16851.pdf)  
**作者**：Ripan Kumar Kundu, Istiak Ahmed, Khaza Anuarul Hoque  

**一句话要点**：提出基于可解释AI引导的差分隐私框架PrivateXR，以防御扩展现实中的隐私攻击。

**关键词**：扩展现实隐私, 可解释AI, 差分隐私, 成员推理攻击, 实时部署

## 3 点简述
- AI XR系统面临成员推理和重识别攻击，差分隐私均匀应用会降低模型性能。
- 利用后验解释识别关键特征，选择性应用差分隐私，减少噪声并提升效率。
- 实验显示攻击成功率降低达43%，模型准确率保持97%，推理时间提升约2倍。

## 摘要（原文）

> The convergence of artificial AI and XR technologies (AI XR) promises innovative applications across many domains. However, the sensitive nature of data (e.g., eye-tracking) used in these systems raises significant privacy concerns, as adversaries can exploit these data and models to infer and leak personal information through membership inference attacks (MIA) and re-identification (RDA) with a high success rate. Researchers have proposed various techniques to mitigate such privacy attacks, including differential privacy (DP). However, AI XR datasets often contain numerous features, and applying DP uniformly can introduce unnecessary noise to less relevant features, degrade model accuracy, and increase inference time, limiting real-time XR deployment. Motivated by this, we propose a novel framework combining explainable AI (XAI) and DP-enabled privacy-preserving mechanisms to defend against privacy attacks. Specifically, we leverage post-hoc explanations to identify the most influential features in AI XR models and selectively apply DP to those features during inference. We evaluate our XAI-guided DP approach on three state-of-the-art AI XR models and three datasets: cybersickness, emotion, and activity classification. Our results show that the proposed method reduces MIA and RDA success rates by up to 43% and 39%, respectively, for cybersickness tasks while preserving model utility with up to 97% accuracy using Transformer models. Furthermore, it improves inference time by up to ~2x compared to traditional DP approaches. To demonstrate practicality, we deploy the XAI-guided DP AI XR models on an HTC VIVE Pro headset and develop a user interface (UI), namely PrivateXR, allowing users to adjust privacy levels (e.g., low, medium, high) while receiving real-time task predictions, protecting user privacy during XR gameplay.

