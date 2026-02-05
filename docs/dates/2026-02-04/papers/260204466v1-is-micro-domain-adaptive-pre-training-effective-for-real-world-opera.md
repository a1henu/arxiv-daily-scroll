---
layout: default
title: Is Micro Domain-Adaptive Pre-Training Effective for Real-World Operations? Multi-Step Evaluation Reveals Potential and Bottlenecks
---

# Is Micro Domain-Adaptive Pre-Training Effective for Real-World Operations? Multi-Step Evaluation Reveals Potential and Bottlenecks
**arXiv**：[2602.04466v1](https://arxiv.org/abs/2602.04466) · [PDF](https://arxiv.org/pdf/2602.04466.pdf)  
**作者**：Masaya Tsunokake, Yuta Koreeda, Terufumi Morishita, Koichi Nagatsuka, Hikaru Tomonari, Yasuhiro Sogawa  

**一句话要点**：评估微领域自适应预训练在生成任务中的潜力与瓶颈，揭示其在知识提取有效但推理不足

**关键词**：微领域自适应预训练, 生成任务评估, 多步分解, 知识提取, 推理能力, 企业应用

## 3 点简述
- 核心问题：微领域自适应预训练在真实企业生成任务中的有效性未知，需评估其潜力与瓶颈。
- 方法要点：将回答过程分解为事实提取、推理和答案撰写三个子任务，进行多步评估。
- 实验或效果：mDAPT解决了基础模型在事实提取上的困难，但未改善推理和撰写任务，强调需增强推理能力。

## 摘要（原文）

> When applying LLMs to real-world enterprise operations, LLMs need to handle proprietary knowledge in small domains of specific operations ($\textbf{micro domains}$). A previous study shows micro domain-adaptive pre-training ($\textbf{mDAPT}$) with fewer documents is effective, similarly to DAPT in larger domains. However, it evaluates mDAPT only on multiple-choice questions; thus, its effectiveness for generative tasks in real-world operations remains unknown. We aim to reveal the potential and bottlenecks of mDAPT for generative tasks. To this end, we disentangle the answering process into three subtasks and evaluate the performance of each subtask: (1) $\textbf{eliciting}$ facts relevant to questions from an LLM's own knowledge, (2) $\textbf{reasoning}$ over the facts to obtain conclusions, and (3) $\textbf{composing}$ long-form answers based on the conclusions. We verified mDAPT on proprietary IT product knowledge for real-world questions in IT technical support operations. As a result, mDAPT resolved the elicitation task that the base model struggled with but did not resolve other subtasks. This clarifies mDAPT's effectiveness in the knowledge aspect and its bottlenecks in other aspects. Further analysis empirically shows that resolving the elicitation and reasoning tasks ensures sufficient performance (over 90%), emphasizing the need to enhance reasoning capability.

