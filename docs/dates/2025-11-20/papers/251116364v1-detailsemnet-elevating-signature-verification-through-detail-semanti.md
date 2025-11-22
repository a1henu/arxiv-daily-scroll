---
layout: default
title: DetailSemNet: Elevating Signature Verification through Detail-Semantic Integration
---

# DetailSemNet: Elevating Signature Verification through Detail-Semantic Integration
**arXiv**：[2511.16364v1](https://arxiv.org/abs/2511.16364) · [PDF](https://arxiv.org/pdf/2511.16364.pdf)  
**作者**：Meng-Cheng Shih, Tsai-Ling Huang, Yu-Heng Shih, Hong-Han Shuai, Hsuan-Tung Liu, Yi-Ren Yeh, Ching-Chun Huang  

**一句话要点**：提出DetailSemNet以提升离线签名验证的准确性和可解释性

**关键词**：离线签名验证, 局部结构匹配, 特征解缠, Transformer架构, 泛化能力, 可解释性

## 3 点简述
- 离线签名验证中，传统方法依赖整体特征，忽略细粒度差异影响鲁棒性。
- 引入Detail Semantics Integrator，通过特征解缠和重缠增强局部细节和语义。
- 在基准测试中实现SOTA性能，并展示优异的泛化能力和可解释性。

## 摘要（原文）

> Offline signature verification (OSV) is a frequently utilized technology in forensics. This paper proposes a new model, DetailSemNet, for OSV. Unlike previous methods that rely on holistic features for pair comparisons, our approach underscores the significance of fine-grained differences for robust OSV. We propose to match local structures between two signature images, significantly boosting verification accuracy. Furthermore, we observe that without specific architectural modifications, transformer-based backbones might naturally obscure local details, adversely impacting OSV performance. To address this, we introduce a Detail Semantics Integrator, leveraging feature disentanglement and re-entanglement. This integrator is specifically designed to enhance intricate details while simultaneously expanding discriminative semantics, thereby augmenting the efficacy of local structural matching. We evaluate our method against leading benchmarks in offline signature verification. Our model consistently outperforms recent methods, achieving state-of-the-art results with clear margins. The emphasis on local structure matching not only improves performance but also enhances the model's interpretability, supporting our findings. Additionally, our model demonstrates remarkable generalization capabilities in cross-dataset testing scenarios. The combination of generalizability and interpretability significantly bolsters the potential of DetailSemNet for real-world applications.

