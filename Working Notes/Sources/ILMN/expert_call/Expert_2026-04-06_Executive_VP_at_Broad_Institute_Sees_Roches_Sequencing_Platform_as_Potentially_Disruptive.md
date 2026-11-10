# **Executive VP at Broad Institute Sees Roche's Sequencing Platform as Potentially Disruptive for Rapid Applications**

DATE PUBLISHED 

20 Apr 2026 

INTERVIEW DATE 

06 Apr 2026 

EXPERT PERSPECTIVE 

Consultant 

ANALYST PERSPECTIVE 

Investor-Led (Buy-Side) 

PRIMARY COMPANY 

Table of contents EXPERT BIO INTERVIEW TRANSCRIPT 

Client 00:00:00 

Thank you for taking the time. I'm interested in learning more about llumina to try to just understand the competitive environment relative to Roche. I know you've got all the competitive instruments at 

the Broad, but have you just as it relates to Roche specifically, have you actually run samples on the Roche Axelios or no? 

Expert 

00:00:22 

Yes, we have. We have a pre-commercial version of the instrument. We had one of the first two that they put out to, basically beta test. They gave us one and they put the other one in the Netherlands at the Hartwig Medical Foundation 

Client 00:00:39 

Okay. Just maybe to step back and I believe you have, you have some Element units as well as some Ultima. Just curious, you guys are you running all these systems for production volumes, all these competitive systems, or are you just testing them and then you give the manufacturer some feedback, but you don't really ever use them for any external genomes that you'd be sequencing? 

Expert 

00:01:02 

We run those platforms, Element and Ultima, but I would not call them at production level. We're not really running them just to give feedback to the vendors. We're really running them, I would say, for specific projects that people have asked us to run on those boxes. It's pretty low volume. Definitely, I would say, not making advance into our production Illumina volume. 

Client 00:01:25 

Got you. Maybe we'll start with the conclusion and then go back through all the steps. Do you see Roche as potentially being a system that you would adopt for production volumes or is it not even here yet? 

Expert 00:01:40 

I would say most likely we will have it in production. It does bring, I would say, more of an advantage to the table than the other platforms have, given the very fast runtime on Roche and the low cost. I do think it's going to be attractive. First of all, for things that really require speed. I would say most of our work right now does not require speed, but we certainly will expand some applications try to release a rapid genome for the NICU setting, you can get a result back same day. That's how fast the machine is. 

That's something that when we think about how we'll adopt Roche, first, I would say it's for incremental. Things that we aren't doing on an Illumina right now. I think over time, there is a good chance that we'll probably try to put more on it, because it does have this very fast runtime, and so, we won't have to batch things as much to get the lower price. That's what we do on the NovaSeq X Plus right now. 

Client 

00:02:39 

That makes sense. It's like maybe clinical. Sounds like the central use case. You mentioned in NICU. I've heard counting applications might be. Why is that? Maybe just help me understand. Again, I should have prefaced. I'm not a scientist by training. Very curious, but a lot of this I don't necessarily know from maybe firsthand experience. 

Expert 

00:03:09 

Counting that's a class of applications. It's not like a whole genome sequencing experiment. You're 

just trying to quantify typically barcodes or other short sequence tags. We would do counting for things like single-cell RNA sequencing. Again, you're just trying to quantify transcripts also for things like the plasma proteomics measures like the Olink or the SomaLogic, that's a counting application because you're just reading a barcode essentially and quantifying the relative amounts of different barcodes that are found in the sample. 

Client 

00:03:41 

I see. That would be the benefit on the counting applications for Roche is the speed. I've read about simplex versus duplex, and they run simplex now where maybe the error rates aren't as critical. Expert 

00:03:54 

That's right, because in barcodes you design them purposefully so that you can withstand a little bit of error is a way to think about it. If you make a mistake and the barcode isn't presented as a possible barcode, then you just use that data you would just throw out. You don't have that super high accuracy requirement. Yes, for counting on the AXELIOs, you would run in simplex mode. 

I think Roche is Being pretty aggressive on pricing. The pricing they announced at the conference last month AGBT. I think people are attracted to what potentially that's going to look like. You're just able to generate a lot of data for a pretty cheap price. If we compare it to Illumina's list price, it's for counting applications, it could be 1/2-1/3 of the cost. It's pretty attractive. There's still things to work out there. 

First of all, the box is not commercial yet. It's still only in this beta version and I don't think it'll be out until later in the year from my understanding. Of course, there's going to will be lots of implementation details, how you actually get this instrument running in production, what the data flow looks like, what the analysis pipeline, what it entails. That still all remains to be determined, but just on the pricing that they've given, it's potentially disruptive. 

Client 

00:05:12 

How disruptive is the devil's in the details is what you're saying. 

Expert 00:05:16 

Exactly. 

Client 00:05:17 

Okay. Can we walk through just the different aspects of the solution. Just starting with the technology, this SBX versus what Illumina does in this expandomers. It sounds super complex, but very maybe scientifically intriguing. How does it work as well as they say? I've heard that their reagent cost is lower than Illumina, but it sounds like based on the real cool chemistry, it would be more expensive. I don't know. 

Expert 00:05:49 It's likely to be cheaper actually than Illumina because of a couple things. Illumina, with sequencing by synthesis, their assay requires fluorescently-labeled nucleotides, because essentially the Illumina sequencer is a big camera or a big microscope where it's recording these fluorescent signals. The read off, the DNA letter A, G, C, or T. They're different colors, essentially. Not only is it expensive to make those nucleotides, we call them, the flow cell itself is a highly engineered. 

You can think of the flow cell like a microscope slide, basically, but it's highly engineered. It has all these little grooves where the clusters are synthesized, and that's how the sequencing gets read out. The flow cell has expense behind it. You have to make these expensive flow cells. That's a reagent. The fluorescent label nucleotides, like I said, those are relatively expensive. 

Roche doesn't use fluorescence. Roche uses basically detection of these expanded molecules through a nanopore, essentially. There's no fancy camera, and there's no fancy labeled nucleotides. Instead, they take the DNA template, and they convert the letters into these expanded molecules which code for the A, G, C, and T. Those expanded molecules expandomers are large. When they pass through the nanopore, it records the signal, basically, that corresponds to a letter. It has the potential to be much cheaper. It's not fluorescent-based. It's using a nanopore detection and not a highly-engineered flow cell. 

Client 00:07:27 

Okay. It sounds conceptually like Oxford Nanopore, but maybe it's not. Maybe there is a difference on that. 

Expert 00:07:37 

No, there's a pretty big difference. Oxford Nanopore passes the DNA itself directly through the pore to try to read the sequence. That works. Oxford's made strides over time. It's much harder to detect straight up DNA, than it is these expanded molecules. Roche is making it easier to use the pore rather than passing through native DNA. 

Client 

00:08:00 

That makes sense. Do you think though that Roche can they move to even larger DNA with the expandomers or is there a limit because of the expandomer being added? The length of the expandomer there number of bases they can read at one point in time is limited. 

Expert 

00:08:18 

It seems like they potentially have headroom to make longer reads than they're offering right now. I don't think that they're going to read long pieces of DNA like Oxford Nanopore does, because again, Oxford Nanopore is reading the direct DNA. I think Roche has headroom, from what I understand. I don't know how long they can get their reads, but probably longer than they are right now. 

Client 

00:08:43 

That makes sense. The SBX chemistry seems to work fine in your hands. You haven't had problems with. I've heard it takes a couple hours longer to prepare the library. Do the library prep. Is that what you found as well? 

Expert 00:09:04 

There'ss two steps. There's a step of making the expandomers and that happens on a different box than the sequencer. There's three parts. There's library prep where you're like putting adapters on the DNA, getting the DNA ready to go and then you're making the expandable molecule itself. That's on the machine. It gets loaded onto the second machine, which is the detection unit. That's where the nanopore cartridge you can think of, it gets loaded. That's where the detection happens. 

Client 

00:09:37 

That second unit is what they'll run in four hours. 

Expert 00:09:41 

That's sequencing right up. That can be four hours. You can run it shorter if you want to. It's tunable to how long you want to run it. You can then be running the expandomer making machine in parallel. You parallelize it. You can always be prepping your next set of expandomers to load onto the instrument. 

Client 00:10:02 

That's interesting. Apologies for not totally knowing exactly how this works, but Illumina, everything happens on the sequencer itself, so you could not do that parallel. 

Expert 

00:10:13 

That's right. The equivalent stuff with Illumina is a step called cluster generation. That's where the DNA fragments get bound onto the flow cell, and then they get locally amplified in these tiny little spots, they call them clusters. That's happening on the flow cell, on the sequencer, and then the sequencing reaction starts and the sequence gets read out. An Illumina run on the NovaSeq X plus, if you're running the 25B flow cell. It takes about 44 hours to run the box. During those 44 hours, both of those steps are happening. 

Client 00:10:50 

I see. Whereas, when we hear someone say, oh, it's a longer sample prep time for Roche than it is for Illumina, but then you save a few, you save hours on the sequencing. In a sense, it's apples and oranges because you could be running the front box. You can get closer to the sequence time in practice in that sense. 

Expert 00:11:12 That's right. It's ultimately going to be considerably faster than Illumina that can generate sequence data. 

Client 00:11:19 

How does someone like yourself think about the speed? Is there a monetary value you might put on that or a customer would put on that? They might say, I'll pay 20% more. 

Expert 00:11:31 

It depends, right. It really depends on the application space. Think about sequencing in the setting of the NICU or intensive care unit, where people want to get the data back the same day to help inform patient care. They'll pay more, because typically those tests are getting reimbursed, and they're getting reimbursed at a pretty high rate, actually. 

I think there will there will be a market for that. It is incremental. It's not the size of the business we have right now on Illumina where we do all of our whole genomes and we do all of our applications now on Illumina. The answer there is, for some of them, no, speed doesn't really matter that much. If you're doing a big single cell RNA sequencing experiment, you don't need the data back the same day. Maybe people would like the data back. That 44-hour runtime, that's not an impediment right now. 

Client 

00:12:28 

Okay. I might not be asking the question correctly, but does the seed somehow create a lower cost or somehow there's more capacity? 

Expert 

00:12:38 

What it does is it allows for more flexibility. I think that the advantage that some people are going to like is that, to achieve the lowest possible cost on Illumina, you run the 25B flow cell and you have to pack it full because you don't want to have wasted space. Airplanes want to have all the seats full on an airplane. Some labs, they will have to wait and put up a batch, and then run the sequencer to be most efficient. 

You can imagine that if the runs are just happening much more quickly, then the batch sizes can be much smaller. Given the pricing that they announced last month, you're going to achieve that low Illumina cost without all the batching. That's what I think potentially could be attractive for a lot of labs. 

Client 

00:13:22 

What does that do for the market? It probably it's a nice to have for you for this, your scale, but are there labs maybe it impacts you in the sense that, a smaller competitor could have the same cost as the Broad. How does it impact the market? 

Expert 

00:13:37 

It's a good question. In many ways, I don't know. Could this further decentralize sequencing that more labs are just going to have access to this and not have to outsource as much? I think that's possible. I do think it's going to take time though, because these smaller labs will also have to build all the surrounding workflows around the box, workflows for DNA preparation, the data analysis, and bioinformatics pipelines. That all is built to be developed and we'll see how that uptake goes. I do think that it has potential to change the market a bit. 

Client 

00:14:13 

Definitely. It sounds like maybe the initial customer base is clinical focus applications and maybe mid-sized labs that might be on the bubble to acquire an X Plus, but haven't yet done it. 

Expert 

00:14:27 

That's possible. With the clinical labs, the question there is like, is it the smaller clinical lab? The more decentralized in Europe a lot of the labs are decentralized that do clinical sequencing or is it the big specialty diagnostics labs like the Caris and Guardant and Tempus, those big labs. For me, that's probably a little bit more questionable, because those guys are so tuned on Illumina and have 

lots of machines. Batching doesn't matter to them. They always have samples to run. Shortening the runtime doesn't save them that much because the whole process, you've got to get the sample, register the sample, return the results. 

Shortening the sequence run down to four hours versus two days probably isn't that much of a win for them. They have to redo all of their validation. That's the bigger thing. You'd have to have all that clinical validation redone, potentially have to go to the FDA depending on what product it is. That's a pretty big list. Whether they'll do it, I don't know. 

Client 00:15:34 

Just to dimension the size of samples running. Say somebody is multiplexing the front box in front of the sequencer and so theoretically you can run the Roche box 10 times in the time that you run the Illumina X Plus, how many samples can you run on that Roche unit on that 10 times one for a run compared to the Illumina unit? 

Expert 00:15:54 

It depends on what kind of sample you're running. If it's simplex or duplex, that'll be different. Both 

the Roche and the Illumina box can do about 20,000 whole genomes. If you were just running genomes. Both boxes can do about, like 20,000 annually. If you think about our Illumina output, so on a 25B, we can get 64 genomes in that 44 hours. With Roche, as you said, you can do many more runs. You can do 10 times the run. It's probably about five or six genomes per run. You're loading them more. You can do five or six, every four hours rather than stretch out the 64 over 44 hours. 

Client 

00:16:39 

It's equivalent throughput on a timed basis in other words. 

Expert 

00:16:43 

Such as the runs come down more often on rush. You're loading the next run 10 times rather than just loading it once. 

Client 00:16:51 

That makes sense. In terms of one other one just on the sample side of things, I'm just wondering, say, one starts to adopt the Roche sequencer. I've heard that theoretically a lab could switch all of its consumables except for the last step on the Illumina instrument. Is that true? In other words, maybe Roche would say, we'll give you a lot lower price on the consumables if you switch all your consumables to us, even the prep for the Illumina instrument. Is that not true? 

Expert 00:17:23 

I'm not quite sure. On Illumina, you must use their flow cell, and you must use the sequencing kit. They come bundled. The sequence kit, plus the flow cell is the consumable Illumina sells. Upfront library prep. We buy from a variety of vendors. We buy it from Roche, we buy it from Watchmaker, we buy it from Kapa. There's different providers of library kits. In front of Roche, we will probably use the Roche kit or we can use other kits. You can only use Roche reagents for the library prep on the Roche machine. You need to use their sequencing kit just like you need to use Illumina sequencing kit on an Illumina machine. Does that make sense? 

Client 00:18:10 

Okay. It's not like Roche can come in and offer some discount on. I'm thinking Roche has such a big business on the regular diagnostic side where they're supplying a ton of chemicals. Maybe they would have some lower price point on the standard chemical workflow. You have to utilize the Illumina at least for the step that goes on to the flow cell. 

Expert 00:18:35 Yes. Client 00:18:36 

That makes sense. In terms of error rates, I've read some articles that talk about the error rates. How has your work found that some of the published research from Roche is accurately representing the error rates? 

Expert 00:18:50 

Again, we're not running it in production right now. They presented some of our data at these conferences too. I can validate that the data is correct. We do see with a duplex about a Q40 error rate, which is very good. It's less accurate to simplex, but perfectly fine for most applications that need that type of sequencing. 

Client 00:19:14 

Okay. You're not finding there's nothing with the error rate that is a systematic bias in their error rates. It is more of a random. 

Expert 00:19:22 

I would say not right now. We've not done super deep analysis of every possible type of sequence context. We've done whole genome sequencing We've done some counting applications and the data is quite good. 

Client 00:19:36 

Great. On my reagent question, adaptive ligation that's the part that's captive to Illumina or will always be captive to Illumina. 

Expert 00:19:45 

No. The thing that's captive to Illumina is their flow cell and the sequencing chemistry, that's Illumina's, that's their product. The upfront steps like adding the adapters, doing the library prep, that can be any company. There's a variety of companies that do that stuff. Illumina sells it too, but it's not solely captured by Illumina. 

Client 00:20:09 

Okay. In terms of data output, does the output that Roche generates? Is that a standard format such that you can run it through any of the available tools, or is it somehow different and you need to then build all your own tools for the data interpretation? 

Expert 

00:20:25 

It's pretty standard. We can run it through our pipelines. There will be steps to do quality control on the data that we'll have to build up custom. In the variant detection algorithms there may be tuning that we'll do eventually once we have lots and lots of more data. It's a very similar type of output that comes off of any sequencer. 

Client 00:20:46 

Okay. Can you run it through the DRAGEN software, or no? Is that somehow you can't do that? 

Expert 

00:20:55 

We wouldn't be able to do that, no. 

Client 00:20:57 

Is that just like a not allowed to otherwise you violate a license agreement or is it actually the data format is different than what you'd need to load it into the DRAGEN? 

Expert 00:21:07 

I suppose you could set up the files that you could put it onto DRAGEN. I don't think we would do that just for not violating the license for those reasons. It has different read lengths, because of the way the sequencing is done. It's going to look a little bit different. You can't just put it blindly into an Illumina pipeline. We will have to use their data processing step to get it ready for the variant detection. 

Client 00:21:34 

Okay. Do they have their own data processing software or is that not yet available? 

Expert 00:21:41 

You have to have your own data processing to get off the sequencer and ready for downstream analysis. That's something they will provide with the box. 

Client 

00:21:50 

Okay. Now, how big a barrier is that to adoption of the Roche sequencer? Is that a huge barrier that you'd be running two of these data processing software programs or is that not a big deal? Expert 

00:22:06 

It'ss not a big deal. It's just part of the way the way the data comes off the sequencer into a processing pipeline. It's just specific to the sequencer. That's not a big deal. We would expect that. 

Client 

00:22:21 

Makes sense. Does Dragon, is it doing variant detection or is that the actual software that does the process of the pipeline itself? 

Expert 00:22:31 

It does both. Dragon is the infrastructure that runs the software, but the software on there does multiple things. There's different types of analysis pipelines that you can run on Dragon. 

Client 00:22:42 

Maybe just as a to come full circle. Can we walk through how price per gigabase with the X Plus versus the Roche, because some of the work I've seen, maybe Illumina doesn't include sample prep. Have you done an apples-to-apples comparison between the two machines to get to a fully loaded cost per gigabase or no? 

Expert 00:23:03 

The list price. Roche said at the conference that the genome they were going to launch for I think a few hundred dollars, is that right? 

Client 00:23:12 I think that's right, yeah. I think that's right. 

Expert 00:23:15 

The whole deal would be a few hundred dollars. That's an all in. From what I understand of course, that's an all in on the sequencer side that's running sequencing reaction they're saying would be a few hundred dollars for a genome. The comparable Illumina would be list price $200 

Client 00:23:34 

It doesn't make sense that Roche would introduce a sequencer at almost double the price per whole genome to Illumina, because they'd never sell anything. I've read some places that the $200 doesn't include the sample prep, chemistry and time and so forth, so it's in apples and oranges. Why would you or anyone else buy something that costs a few hundred dollars for the output versus Illumina is $200 

Expert 

00:24:03 

No, I think that that's right. Once you tack everything else on to Illumina. We sell our Illumina genome for less than $400 and that's fully loaded, like labor, all the reagents, doing the initial variant calling. Roche is going to be a bit more expensive. If I'm remembering that few hundred dollar number correctly. 

No, sorry, I got that wrong. They announced $150 at AGBT. That makes more sense to what I said. 

Client 

00:24:33 The $200 itself, I was characterizing it correctly. It's not a fully loaded cost. 

Expert 00:24:40 That's right. That's just the cost of the sequencing. $2 per gig is what the flow cell and sequencing consumables cost on Illumina list price 25B. You would compare that to the $150 that Roche said. 

Client 

00:24:55 

Okay. The $150 would be a similar. Yes, just the sequencing plus the consumables and so forth. 

Expert 

00:25:05 

I would compare  150 − 200. 

Client 00:25:09 

Perfect. Anything else on the Roche side that we didn't talk about in terms of as you think about evaluating potentially bringing on a Roche sequencer for production? stuff like that. 

Expert 00:25:21 

The stuff that I would say that we don't understand completely yet is some of the stuff about dataflow, because it is so much data generated so quickly. I think we are trying to figure out what that will look like in terms of the transfer rate of the data, how we're going to build out that pipeline so that the data is flowing into the cloud or however we do the processing. That's the stuff we're going to have to learn once we get the commercial version of the box and the commercial version of the bioinformatics pipeline. 

Client 

00:25:49 

Perfect. Maybe just high level on Element. Where do you think that box fits in the sequencing landscape? Is there a place for that box? It's more of a mid throughput as I understand it. That box, how you guys found that one? The Element. 

Expert 

00:26:09 

It hasn't honestly hasn't found much of a place with us. We have a very strong Illumina discount on their mid throughput box as well. It hasn't really differentiated itself I would say at the Broad. We just have pretty low utilization of it as a benchtop machine. 

Client 

00:26:26 

Okay. How about the Ultima box seems maybe a me too Roche box in terms of the way it operates and so forth. Is that, or am I maybe mischaracterizing it? 

Expert 

00:26:37 

Ultima it is different than Roche. It is a high throughput machine as well. They don't do the duplex sequencing or anything. It's still, that's just, they still do the single end sequencing, but good accuracy overall. Ultima themselves announced some pretty interesting, I would say improvements on the system, they announced at AGBT. You don't have to use that second box to do what they call their amp step. You can do it on off-the-shelf automation. 

There's no emulsion PCR anymore. They figured out a different way to get the DNA on the beads. I think that's going to improve their overall workflow. I think that's been a step people have complained about over time. I think they've made some improvements in the sequencing chemistry too. I think there's people who are happy with their data quality. They're putting out this new box. I think it's the UG200 or UG2000, I forget the numbers. 

I think that we still are pretty much just using the Ultima systems, I would say in a pretty low throughput way. We don't have a ton of volume going through them, and it's pretty much focused on just a couple projects that specifically wanted to use the Ultima box. One around sequencing ancient fragmented DNA from ancient humans. We have a researcher who is very interested in that. We also run some of the plasma proteomics like the Olink assay we run on the Ultima box. We run it on Illumina too, but we have one user who really wanted to use the Ultima box. 

Client 00:28:12 

Interesting. I'm just curious those two use cases. Why did they want the Ultima box and what was it about the features, functions of Ultima that drew them to that box? Expert 

00:28:24 Special pricing. 

Client 00:28:26 

I see. Did you ultimately think go to the researchers and say, "Hey, if you run it on our box, we'll give you a special price via the we'll extend that to the Broad, and you'll get that lower price as a result?" Expert 00:28:43 Yes. Client 00:28:44 I see. Is the ancient fragmented DNA a high-throughput application or somehow. Expert 00:28:52 No. 

Client 00:28:53 It doesn't it would be. 

Expert 00:28:56 

No. It's pretty specialized. He has thousands of these samples, believe it or not, and then this is DNA from ancient humans like 40,000 years ago or something. He does have thousands of samples of masks. He has funding and he's doing whole genomes at a pretty good price. The data quality for what he needs is actually very good, but he's happy with it. 

Client 00:29:20 

Is the data quality better than it would be on Illumina or is it just purely the pricing? Expert 00:29:27 

He was able to work in this specific example. Work with the Ultima team and customize the data analysis for what he needed specifically, because his DNA has a different error pattern because how fragmented it is. They've been able to partner to make a nice software package that does really well which his data type. Could you have done that on Illumina? Sure. He has to be working with Ultima to do that, 

Client 00:29:55 

To get that attention, that bespoke software development, in other words. 

Expert 00:30:01 

Yeah, that's the way I think about it. 

Client 

00:30:04 

That makes sense. Just different question, how do you see the research growth in samples on the research side for you guys or the market in general? How fast are we growing and are some of the new pricing coming out of Illumina accelerating growth? Is the XP itself accelerating growth and then maybe some of the pricing and the flow cells that's changed, helping drive growth. Expert 

00:30:30 

It's complicated because we are worried about the NIH situation. Very few new grants are getting funded even though they are still funding existing awards. I think that that is likely going to impact growth over the next couple years unless things turn around. It's a weird situation because the NIH does have good bipartisan support in terms of they've agreed to try to keep the budget flat even though Trump is proposing additional cuts. I don't know if those will happen or not, but the problem is, they're just not getting the money out of the NIH the way they used to. 

I think I saw a number over the weekend where across the country fewer new grants have been funded this year, whereas, in most years many more would be funded by this point. The number of new awards is just dramatically lower. We are always seeking differentiated, we're trying to diversify our funding sources. Not depending so much on the NIH, but really counting on industry sponsored sequencing projects from pharma companies, biotech companies, also philanthropy like disease foundations often will want to fund genomics projects. With that said, growth is hard to really count on. I think we've seen decent demand. 

A number I like to quote for people is, I think when we looked at 2024-2025 our IIlumina spend was basically flat year over year, but we generated twice as much data. That's good. It's not like we just spent half the money so we could get the same amount of data. People are still hungry for sequence data. It's not like it's growing, it's not doubling, but the spend is staying flat. The volume we're producing is increasing a lot, which is great. As the sequencing prices are getting lower and lower, people start to imagine doing bigger projects than they would have or different types of projects. 

An area we think there could be growth is in what we consider multi-omics. Doing different RNA sequencing or methylation sequencing. Single-Cell RNA sequencing is a potential big area, because the prices have come down so much, people are starting to talk about doing pretty big projects. Although, I would not say we have a ton materializing yet, we're certainly out there talking. Particularly to pharma companies about this. Tech companies are interested in this data for the AI models. Hopefully, that'll be a good trend for the upcoming year or two Client 

00:32:54 

Clinical is that, or is that just too small for you guys? 

Expert 

00:32:58 

We do some clinical sequencing, but it's small. We're not there trying to compete with like the Caris and Guardant, Tempus. Those are big diagnostic companies that have the big sales force and the doctor ordering capabilities. We don't have that. We do some back-end sequencing for some commercial labs that is clinical, but it's not a big driver for us at the moment. 

Client 00:33:19 

It doesn't sound like it's given that the complexities of the market and the existing competitors, something that you would target either really as a growth. 

Expert 00:33:29 

We just don't have the sales channels. That's what you need to compete in those markets where you're trying to have physicians order your test. We don't have the people out there selling to physicians all over the country. 

Client 00:33:41 

The hospitals themselves or independent diagnostic labs probably don't have those tests either because they're all gotten approval by companies. 

Expert 00:33:49 

Hospitals are using those labs. They don't necessarily need to come to us. We have some local partnerships with our local like Dana-Farber investigators. Some of them are developing some custom or their own assays and we will do those under a clinical framework. It's not a huge volume driver for us. It's just something we do. We'd be good partners with the local hospitals. 

Client 00:34:14 

That makes sense. The doubling of data with flattish spend from Illumina, is that literally just say your price is half what it was or have you made changes in your own workflow and where maybe you source chemicals from or to enable some portion of that 50%? 

Expert 00:34:31 

That's mostly the transition to the NovaSeq X Plus 25B. It's about Illumina's prices come down, because the previous year in 2024, we were still doing some of our projects on the 6,000, but by 2025, we had fully transitioned off. 

Client 00:34:48 

Okay. What does it look like for rough numbers for 2026 just out of curiosity, then, if that transition's happened, is there underlying volume growth now on a like-for-like basis your spend with Illumina goes up or no? 

Expert 

00:35:03 

Unlikely, because we haven't added any machines. Our machines right now are pretty full. We're typically in the upper double digit percentage. We could only spend more with Illumina if we bought machines, which we are unlikely to do, unless, some new big funding shows up. At our current four forecast, I would say we're probably fine with the number of machines we have now, and I would say there's some unknowns in the back half of the year. Again, given what happens with the NIH, if some of our bigger projects start to get cut, then perhaps could be spending less, but I would say it's too soon to tell right now. 

Client 

00:35:42 

Got it. This was super helpful. I appreciate the time and your patience. This was super helpful to me. Much appreciated. 
