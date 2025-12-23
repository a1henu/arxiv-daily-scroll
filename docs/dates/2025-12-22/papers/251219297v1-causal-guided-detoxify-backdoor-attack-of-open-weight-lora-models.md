---
layout: default
title: Causal-Guided Detoxify Backdoor Attack of Open-Weight LoRA Models
---

# Causal-Guided Detoxify Backdoor Attack of Open-Weight LoRA Models
**arXiv**：[2512.19297v1](https://arxiv.org/abs/2512.19297) · [PDF](https://arxiv.org/pdf/2512.19297.pdf)  
**作者**：Linzhi Chen, Yang Sun, Hongru Wei, Yuqi Chen  

**一句话要点**：提出因果引导的去毒后门攻击框架，针对开放权重LoRA模型的安全漏洞。

**关键词**：LoRA后门攻击, 因果引导, 去毒策略, 开放权重模型, 安全漏洞, 隐蔽攻击

## 3 点简述
- 核心问题：开放权重LoRA模型易受恶意适配器攻击，现有后门方法不适用。
- 方法要点：通过覆盖引导数据生成和因果引导去毒策略，实现无训练数据的高隐蔽攻击。
- 实验或效果：在六个LoRA模型上验证，攻击成功率高，误触发率降低50-70%，抗防御能力强。

## 摘要（原文）

> Low-Rank Adaptation (LoRA) has emerged as an efficient method for fine-tuning large language models (LLMs) and is widely adopted within the open-source community. However, the decentralized dissemination of LoRA adapters through platforms such as Hugging Face introduces novel security vulnerabilities: malicious adapters can be easily distributed and evade conventional oversight mechanisms. Despite these risks, backdoor attacks targeting LoRA-based fine-tuning remain relatively underexplored. Existing backdoor attack strategies are ill-suited to this setting, as they often rely on inaccessible training data, fail to account for the structural properties unique to LoRA, or suffer from high false trigger rates (FTR), thereby compromising their stealth. To address these challenges, we propose Causal-Guided Detoxify Backdoor Attack (CBA), a novel backdoor attack framework specifically designed for open-weight LoRA models. CBA operates without access to original training data and achieves high stealth through two key innovations: (1) a coverage-guided data generation pipeline that synthesizes task-aligned inputs via behavioral exploration, and (2) a causal-guided detoxification strategy that merges poisoned and clean adapters by preserving task-critical neurons. Unlike prior approaches, CBA enables post-training control over attack intensity through causal influence-based weight allocation, eliminating the need for repeated retraining. Evaluated across six LoRA models, CBA achieves high attack success rates while reducing FTR by 50-70\% compared to baseline methods. Furthermore, it demonstrates enhanced resistance to state-of-the-art backdoor defenses, highlighting its stealth and robustness.

