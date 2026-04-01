#1.0 Search:
	def UseItemSlot(self, slotIndex):
		curCursorNum = app.GetCursor()
		if app.SELL == curCursorNum:
			return

		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS():
			return
			
#1.1 Add under:

		#BONUS SWITCHER
		if constInfo.IS_BONUS_CHANGER:
			return
		#END OF BONUS SWITCHER
		
#2.0 Search:
	def SelectEmptySlot(self, selectedSlotPos):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return
		
		#BONUS SWITCHER
		if constInfo.IS_BONUS_CHANGER == TRUE:
			return
		#END OF BONUS SWITCHER
		
#3.0 Search:
	def SelectItemSlot(self, itemSlotIndex):
	
#3.1 Add over:
	#BONUS SWITCHER
	def IsChanger(self, itemVnum):
		changerList = [71084] #Vnum bonus changer.
		if itemVnum in changerList:
			return TRUE
		
		return FALSE
	#END OF BONUS SWITCHER
	
#4.0 Search:
	def SelectItemSlot(self, itemSlotIndex):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return

#4.1 Add under:

		#BONUS SWITCHER
		if constInfo.IS_BONUS_CHANGER == TRUE:
			return
		#END OF BONUS SWITCHER
		
#5.0 Search in def SelectItemSlot(self, itemSlotIndex):
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemVID = mouseModule.mouseController.GetAttachedItemIndex()

#5.1 Add under:
			#BONUS SWITCHER
			if self.IsChanger(attachedItemVID) and not player.IsEquipmentSlot(itemSlotIndex):
				itemVnum = player.GetItemIndex(itemSlotIndex)
				item.SelectItem(itemVnum)
				if item.GetItemType() == item.ITEM_TYPE_WEAPON or item.GetItemType() == item.ITEM_TYPE_ARMOR:
					self.interface.AddToBonusChange(itemSlotIndex, attachedSlotPos)
					mouseModule.mouseController.DeattachObject()
					return
			#END OF BONUS SWITCHER