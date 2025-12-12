---
layout: default
title: Authority Backdoor: A Certifiable Backdoor Mechanism for Authoring DNNs
---

# Authority Backdoor: A Certifiable Backdoor Mechanism for Authoring DNNs
**arXiv**：[2512.10600v1](https://arxiv.org/abs/2512.10600) · [PDF](https://arxiv.org/pdf/2512.10600.pdf)  
**作者**：Han Yang, Shaofeng Li, Tian Dong, Xiangyu Xu, Guangchi Liu, Zhen Ling  

**一句话要点**：提出Authority Backdoor机制，通过嵌入访问约束主动保护DNN模型免受未授权使用。

**关键词**：深度神经网络保护, 主动访问控制, 后门学习, 可认证鲁棒性, 模型安全

## 3 点简述
- 核心问题：现有DNN保护方法如数字水印被动，无法主动防止模型被盗用。
- 方法要点：利用后门学习框架，模型仅在特定触发下正常，否则性能退化，结合可认证鲁棒性防移除。
- 实验或效果：在多种架构和数据集上验证了有效性和可认证鲁棒性。

## 摘要（原文）

> Deep Neural Networks (DNNs), as valuable intellectual property, face unauthorized use. Existing protections, such as digital watermarking, are largely passive; they provide only post-hoc ownership verification and cannot actively prevent the illicit use of a stolen model. This work proposes a proactive protection scheme, dubbed ``Authority Backdoor," which embeds access constraints directly into the model. In particular, the scheme utilizes a backdoor learning framework to intrinsically lock a model's utility, such that it performs normally only in the presence of a specific trigger (e.g., a hardware fingerprint). But in its absence, the DNN's performance degrades to be useless. To further enhance the security of the proposed authority scheme, the certifiable robustness is integrated to prevent an adaptive attacker from removing the implanted backdoor. The resulting framework establishes a secure authority mechanism for DNNs, combining access control with certifiable robustness against adversarial attacks. Extensive experiments on diverse architectures and datasets validate the effectiveness and certifiable robustness of the proposed framework.

