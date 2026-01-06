---
layout: default
title: UnPII: Unlearning Personally Identifiable Information with Quantifiable Exposure Risk
---

# UnPII: Unlearning Personally Identifiable Information with Quantifiable Exposure Risk
**arXiv**：[2601.01786v1](https://arxiv.org/abs/2601.01786) · [PDF](https://arxiv.org/pdf/2601.01786.pdf)  
**作者**：Intae Jeon, Yujeong Kwon, Hyungjoon Koo  

**一句话要点**：提出UnPII方法，基于PII风险指数优先遗忘敏感信息以应对隐私法规要求。

**关键词**：机器遗忘, 隐私保护, PII风险指数, 合成数据集, 梯度上升, 偏好优化

## 3 点简述
- 核心问题：现有遗忘技术未考虑不同PII属性的隐私风险差异，难以满足GDPR等法规的删除需求。
- 方法要点：引入PII风险指数（PRI），综合评估多维度风险因素，指导个性化遗忘策略。
- 实验或效果：在合成PII数据集上验证，UnPII集成现有算法提升准确性、效用和泛化性，微调开销适中。

## 摘要（原文）

> The ever-increasing adoption of Large Language Models in critical sectors like finance, healthcare, and government raises privacy concerns regarding the handling of sensitive Personally Identifiable Information (PII) during training. In response, regulations such as European Union's General Data Protection Regulation (GDPR) mandate the deletion of PII upon requests, underscoring the need for reliable and cost-effective data removal solutions. Machine unlearning has emerged as a promising direction for selectively forgetting data points. However, existing unlearning techniques typically apply a uniform forgetting strategy that neither accounts for the varying privacy risks posed by different PII attributes nor reflects associated business risks. In this work, we propose UnPII, the first PII-centric unlearning approach that prioritizes forgetting based on the risk of individual or combined PII attributes. To this end, we introduce the PII risk index (PRI), a composite metric that incorporates multiple dimensions of risk factors: identifiability, sensitivity, usability, linkability, permanency, exposability, and compliancy. The PRI enables a nuanced evaluation of privacy risks associated with PII exposures and can be tailored to align with organizational privacy policies. To support realistic assessment, we systematically construct a synthetic PII dataset (e.g., 1,700 PII instances) that simulates realistic exposure scenarios. UnPII seamlessly integrates with established unlearning algorithms, such as Gradient Ascent, Negative Preference Optimization, and Direct Preference Optimization, without modifying their underlying principles. Our experimental results demonstrate that UnPII achieves the improvements of accuracy up to 11.8%, utility up to 6.3%, and generalizability up to 12.4%, respectively, while incurring a modest fine-tuning overhead of 27.5% on average during unlearning.

