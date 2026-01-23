---
layout: default
title: Rethinking Drug-Drug Interaction Modeling as Generalizable Relation Learning
---

# Rethinking Drug-Drug Interaction Modeling as Generalizable Relation Learning
**arXiv**：[2601.15771v1](https://arxiv.org/abs/2601.15771) · [PDF](https://arxiv.org/pdf/2601.15771.pdf)  
**作者**：Dong Xu, Jiantao Wu, Qihua Pan, Sisi Yuan, Zexuan Zhu, Junkai Ji  

**一句话要点**：提出GenRel-DDI框架，通过关系中心学习解决药物相互作用预测泛化难题。

**关键词**：药物相互作用预测, 关系学习, 泛化能力, 深度学习, 药物发现, 临床开发

## 3 点简述
- 现有药物相互作用模型泛化能力差，难以处理未见药物和稀缺验证数据。
- 将预测重构为关系中心学习，独立于药物身份学习交互表示以捕获可迁移模式。
- 在严格实体分离评估中显著优于现有方法，突显关系学习对稳健预测的有效性。

## 摘要（原文）

> Drug-drug interaction (DDI) prediction is central to drug discovery and clinical development, particularly in the context of increasingly prevalent polypharmacy. Although existing computational methods achieve strong performance on standard benchmarks, they often fail to generalize to realistic deployment scenarios, where most candidate drug pairs involve previously unseen drugs and validated interactions are scarce. We demonstrate that proximity in the embedding spaces of prevailing molecule-centric DDI models does not reliably correspond to interaction labels, and that simply scaling up model capacity therefore fails to improve generalization. To address these limitations, we propose GenRel-DDI, a generalizable relation learning framework that reformulates DDI prediction as a relation-centric learning problem, in which interaction representations are learned independently of drug identities. This relation-level abstraction enables the capture of transferable interaction patterns that generalize to unseen drugs and novel drug pairs. Extensive experiments across multiple benchmark demonstrate that GenRel-DDI consistently and significantly outperforms state-of-the-art methods, with particularly large gains on strict entity-disjoint evaluations, highlighting the effectiveness and practical utility of relation learning for robust DDI prediction. The code is available at https://github.com/SZU-ADDG/GenRel-DDI.

